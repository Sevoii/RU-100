library(tidyverse)

set.seed(1234)

data <- read_csv("data/bootstrap_ci.csv")

# Elbow Method
# Optimal: 3-4 different clusters

# explained_ss <- rep(NA, 10)
# for(k in 1:10){
#   # run k-means on the data
#   clustering <- kmeans(data$Median_Win_Rate, k)
#   explained_ss[k] <- clustering$betweenss / clustering$totss
# }
#
# ggplot() +
#   aes(x=1:10, y=1-explained_ss) +
#   geom_line() +
#   geom_point() +
#   labs(x="Number of Clusters",
#        y="Remaining Variation",
#        title="K-Means Clustering Performance") +
#   theme(text=element_text(size=18)) +
#   scale_x_continuous(breaks=1:10) +
#   scale_x_continuous(breaks=1:10)


clustering <- kmeans(data$Median_Win_Rate, 4)
data <- data %>% mutate(cluster = clustering$cluster)

write.csv(data, "data/kmeans_win_rate.csv", row.names=FALSE)