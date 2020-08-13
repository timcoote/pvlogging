library (magrittr)
library (ggvis)

mtcars %>% ggvis (x=~wt, y=~mpg) %>% layer_points()
