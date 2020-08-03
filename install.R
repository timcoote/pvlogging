# use Vagrantfile 
# install.packages ("devtools")
require(devtools)
install_version("ggvis", version = "0.4.5")
# some of these are causing other packages to be updated....
install_version("dplyr", version = "0.8.3")
install_version("shiny", version = "1.4.0.2")
install_version("htmltools", version = "0.4.0")
# moved to end, as I think that the dependencies are satisfied above
#install.packages ("ggvis")

library (magrittr)
library (ggvis)

mtcars %>% ggvis (x=~wt, y=~mpg) %>% layer_points()
