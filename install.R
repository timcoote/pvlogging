#install.packages ("devtools")
require(devtools)
#install.packages ("ggvis")
install_version("ggvis", version = "0.4.5")
#install_version("dplyr", version = "0.8.3")
#install_version("shiny", version = "1.4.0.2")
#install_version("htmltools", version = "0.4.0")

library (magrittr)
library (ggvis)

mtcars %>% ggvis (x=~wt, y=~mpg) %>% layer_points()
