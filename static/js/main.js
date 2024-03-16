function getWeather() {
    let city = document.getElementById("city_input").value;

    fetch(`https://webarchitect.onrender.com/weather/${city}/`)
      .then(response => response.json())
      .then(data => {


        let temperature = data['temperature'];
        let clouds = data['description'];
        let pressure = data['pressure'];
        console.log(temperature)

        document.getElementById("get_temp").innerHTML = temperature.toFixed(1) + "°C";
        document.getElementById("myclouds").innerHTML = clouds.toUpperCase();
        document.getElementById("pressure").innerHTML = pressure+"hPa";
      })
      .catch(err => {
        console.log(err);
      });
  }
