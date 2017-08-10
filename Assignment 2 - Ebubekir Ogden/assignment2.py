
sensor_values = [80, 75.5, 40.1]


def createWebPage():
    return """
        <html lang="en">
        <head>
      <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no">
      <title>30402.(007) - Assignment 1 - Ebubekir Ogden</title>
      <meta charset="utf-8">
      <meta name="author" content="Ebubekir Ogden">
      <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js"></script>
      <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/css/bootstrap.min.css">
      <link rel="stylesheet" href="assignment1.css">
      <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/js/bootstrap.min.js"></script>
      <script async type="text/javascript" src="assignment1.js"></script>
  </head>

  <body onload="updateUI()">

    <div class="container">

      <div class="row">
          <div class="col-xs-12 col-sm-12 col-md-12 col-lg-12">
            <h1 id="headSensor" class="centerPosition"> Dynamic Sensor Values </h1>
          </div>

      </div>
      <div class="row">
          <div class="col-xs-6 col-sm-6 col-md-6 col-lg-6 centerTablePosition">
              <div class="table-responsive">
                <table class="table table-bordered">
                    <tr>
                        <td class="active cellText">Temperature</td>
                        <td class="active cellText">Pressure</td>
                        <td class="active cellText">Humidity</td>
                    </tr>
                        <td class="active cellText" id="tempValue" onclick="showModal('temp')">{0}</td>
                        <td class="active cellText" id="presValue" onclick="showModal('pressure')">{1}</td>
                        <td class="active cellText" id="humidValue" onclick="showModal('humidity')">{2}</td>
                    <tr>

                    </tr>
                </table>
              </div>

          </div>
      </div>
    </div>

       </body>
       </html>"""
     
    
def main():
    page = createWebPage()
    formatMyString(page)

    
def formatMyString(own_str):
    own_str = own_str.format(sensor_values[0], sensor_values[1], sensor_values[2])
    writeToFile(own_str)

def writeToFile(str_own):
    myFile = open("assignment2.html", "w")
    myFile.write(str_own)
    myFile.close();

main()
