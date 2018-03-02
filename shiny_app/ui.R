## Irene Chen
## Feb 2018

## Creating the UI for the shiny app:

library(shiny)
library(plotly)

shinyUI(fluidPage(
  
  titlePanel("Analysing the Dynamics of the Animated Movie Industry"),
  
  # Slider input for movie year of release, 
  # followed by radio buttons to select which team should be displayed
  
  sidebarLayout(
    sidebarPanel(
       sliderInput("year",
                   "Year:",
                   min = 1980,
                   max = 2016,
                   value = 2010,
                   step = 1, sep=""),
       radioButtons("team", "Select a Team", 
                    c("All Crew"="num_crew", "Animation"="num_animators", 
                      "Visual Effects"="num_visual_fx", "Art"="num_artists",
                      "Writing"="num_writers", "Producers"="num_producers"
                      ))
    ),
    
    # Output a bubble plot,
    # Followed by some statistics:
    
    mainPanel(
       plotlyOutput("bubblePlot"),
       tabsetPanel(
         tabPanel("Statistics",
                  p(h4("Median IMDb Rating for this year:")),
                  textOutput("median_rating"),
                  p(h4("Total # of Animated Movies for this year:")),
                  textOutput("num_movies"))
    ))
  )
))