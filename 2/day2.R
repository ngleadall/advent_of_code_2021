
x <- 0
y <- 0
a <- 0

con = file("./test" , "r")

while ( TRUE ) {
    line = readLines(con, n = 1)
    
    if ( length(line) == 0 ) {
      break
    }
    
    l <- strsplit(line, "\\s+")

    key <- l[[ 1 ]][1]
    val <- as.integer( l[[ 1 ]][2] ) 

    if ( key == "forward" ) {
        y <- y + (a * val )
        x <- x + val
    }

    if ( key == "up" ) {
        a <- a - val
    }

    if ( key == "down" ) { 
        a <- a + val
    }

}

sprintf("x: %s , y: %s , position: %s", x , y, (x * y ))
