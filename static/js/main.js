function getWeather() {
    let city = document.getElementById("city_input").value; // Get city from input field

    fetch(`http://127.0.0.1:8000/weather/${city}/`)
      .then(response => response.json())
      .then(data => {
        // Update city name in header
        document.getElementById("city_name").innerHTML = city.toUpperCase();

        let temperature = data['temperature'];
        let clouds = data['description'];
        let pressure = data['pressure'];
        console.log(temperature)

        // Update HTML elements with weather data
        document.getElementById("get_temp").innerHTML = temperature.toFixed(1) + "°C";
        document.getElementById("myclouds").innerHTML = clouds.toUpperCase();
        document.getElementById("pressure").innerHTML = pressure+"hPa";
      })
      .catch(err => {
        // Display errors in console
        console.log(err);
      });
  }
