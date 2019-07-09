library(limma)
library(edgeR)
library(jsonlite)


count_cols <- c('Normal-1','Normal-2','Normal-3','Normal-4','Normal-5','Tumour-1','Tumour-2','Tumour-3','Tumour-4','Tumour-5')

x<-read.delim('tcga_raw_counts.csv', sep=",", check.names=FALSE, colClasses='character', na.strings=c())

# Now re-read the first header line.  Workaround R problem that always has strip.white=T for read.table
colnames(x) <- scan('tcga_raw_counts.csv', what="", sep=",", nlines=1,strip.white=F, quote = "\"")

x[,count_cols] <- apply(x[,count_cols], 2, function(v) as.numeric(v))     # Force numeric count columns
counts <- x[, count_cols]
keepMin <- apply(counts, 1, max) >= 0.0
keepCpm <- rowSums(cpm(counts)> 0.0) >= 0.0                  # Keep only genes with cpm above x in at least y samples
keep <- keepMin & keepCpm
x <- x[keep,]
counts <- counts[keep,]
design <- matrix(c(c(1,1,1,1,1,0,0,0,0,0),c(0,0,0,0,0,1,1,1,1,1)), ncol=2, dimnames=list(c('Normal-1','Normal-2','Normal-3','Normal-4','Normal-5','Tumour-1','Tumour-2','Tumour-3','Tumour-4','Tumour-5'),c('Normal','Tumour')))


cont.matrix <- matrix(c(c(-1,1)), ncol=1, dimnames=list(c('Normal','Tumour'),c('Tumour')))

y <- DGEList(counts=counts)

y <- calcNormFactors(y, method="TMM")

y <- estimateGLMCommonDisp(y,design)
y <- estimateGLMTrendedDisp(y,design)
y <- estimateGLMTagwiseDisp(y,design)

fit <- glmFit(y,design)
lrt <- glmLRT(fit, contrast=cont.matrix)

out <- topTags(lrt, n=Inf, sort.by='none')$table

lfc <- as.matrix(out[, c(1:ncol(cont.matrix))])
colnames(lfc) <- colnames(cont.matrix)

# Output with column names for degust
out2 <- cbind(lfc,
              'P.Value'   = out[,'PValue'],
              'adj.P.Val' = out[,'FDR'],
              'AveExpr'   = out[,'logCPM'],
              x[, c(c('Gene','Normal-1','Normal-2','Normal-3','Normal-4','Normal-5','Tumour-1','Tumour-2','Tumour-3','Tumour-4','Tumour-5'))] )

write.csv(out2, file="output_dir/output.txt", row.names=FALSE,na='')

cat(
  toJSON(list(prior_df=lrt$prior.df,
              design=data.frame(lrt$design)
  )),
  file="output_dir/extra.json"