let city = "Manchester"; // Since you're fetching weather data for Tashkent

  function getWeather() {
    fetch(`http://127.0.0.1:8000/weather/${city}/`)
      .then(response => response.json())
      .then(data => {
        // console.log(data);

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

