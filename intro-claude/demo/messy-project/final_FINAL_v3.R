# analysis - use THIS version (per email from advisor 3/14)
dat <- read.csv("data (1).csv")
summary(dat$response)
mean(dat$response, na.rm = TRUE)
# TODO: redo the plot, see plot1.png for the old one
