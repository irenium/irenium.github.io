## Irene Chen
## Feb 2018

## Analyze the input data for the shiny app:

library(shiny)
library(plotly)

# Open the data file:
file <- list.files(pattern="moviedf.csv", full=TRUE)
df <- read.csv(file, header=TRUE, sep=",")

shinyServer(function(input, output) {

  # Specify what data should be plotted, based on the user input:
  output$bubblePlot <- renderPlotly({
    year_input <- input$year
    df_by_yr <- df[(df["year"] == year_input),]
    team_select <- input$team

    movie_plot <- plot_ly(x=df_by_yr$rating, y=df_by_yr[,team_select], mode="markers", size=df_by_yr$gross, text = ~paste(df_by_yr$title), color= ~df_by_yr$gross, marker=list(sizeref=0.1))
    layout(movie_plot, xaxis=list(title="IMDb Rating", range=c(4,9)), yaxis=list(title="Team Size [# of people]"))
  })
  
  # Output some simple statistics (median IMDb rating and total number of movies released that yr)
  output$num_movies <- renderText({
    year_input <- input$year
    df_by_yr <- df[(df["year"] == year_input),]
    paste(nrow(df_by_yr))
  })
  output$median_rating <- renderText({
    year_input <- input$year
    df_by_yr <- df[(df["year"] == year_input),]
    paste(median(as.numeric(df_by_yr$rating)))
  })
})
