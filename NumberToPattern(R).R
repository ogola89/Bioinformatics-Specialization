NumberToPattern <- function(number,length){
  pattern <- rep("x",length)
  for(i in 1:length){
    division <- number %/% 4^(length-i)
    if(division == 0 ){pattern[i]="A" }
    if(division == 1 ){pattern[i]="C" }
    if(division == 2 ){pattern[i]="G" }
    if(division == 3 ){pattern[i]="T" }
    number <- number- division* (4^(length-i))
  }
  return(paste(pattern,collapse = ""))
}