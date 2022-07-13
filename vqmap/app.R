library(shiny)
library(shinydashboard)
library(leaflet)
# library(rgdal)
library(dplyr)
library(sf)
library(viridisLite)
library(ineq)



data  = st_read('../../geodata/district_res_jul4.gpkg')
data <- st_transform(data, crs = 4326)


ui = dashboardPage(
  skin = 'black',
  dashboardHeader(title = 'ViewSeeker'),
  dashboardSidebar(
    # sliderInput("q.threhold",label = 'q.threshold', 
    #             min = 0, max = 1, 
    #             value = c(0,1),
    #             sep = "",
    #             step = .01),
    # selectInput("pred", "Choose Variable", choices = c(poi_cols, pred_cols)
    #             ),
    selectInput("agg", "Choose Agg", choices = c("rich","prob","cv","gini","med","avg")
    )
  ),
  dashboardBody(fluidRow(box(width = 12,leafletOutput(outputId = 'ch_map'))))
  
)

# Define server logic required to draw a histogram
server <- function(input, output) {
  data_input = reactive({
    # df = with(dat_, aggregate(input()$pred ~ OBJECTID, FUN =  function(x) {
    #   c( rich = calcRichness(x), oddsr = calcOddsR(x), gini = calcGini(x), MN= mean(x) )} ) )
    # 
    # df = merge( ch_commune,df, by =  "OBJECTID")
    # df = do.call(data.frame, df) %>% st_as_sf
    # return(df)
    
    
    data %>% mutate(output = input$rich) %>% mutate(output = input$agg)
  })
  
  
  # pal = colorNumeric(palette = viridis(100), domain = data_input()$output)
  # input_feat = paste(input()$pred,input()$agg,sep = '.')
  
  output$ch_map = renderLeaflet(
    leaflet(data_input()) %>%
      # setView() %>%
      addProviderTiles(providers$Stamen.Toner) %>%
      addPolygons()
    
    # addCircleMarkers(lat = ~data_input()$Y, 
    #                  lng = ~data_input()$X,
    #                  color = ~pal(data_input()$pred_clf)) %>%
    # addLegend("bottomright",
    #           pal = pal,
    #           values = data_input()$pred_clf,
    #           title = "Pred_Clf",
    #           opacity = 1) 
  )
  
  
  
}





# Run the application 
shinyApp(ui = ui, server = server)
