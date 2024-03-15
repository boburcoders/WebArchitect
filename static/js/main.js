
let city = "Tashkent";
let api_key = 'b19ef47e383821acf92694c11bf2f394';
let lat = 53.4795;
let lon = -2.2451;

function getWeather() {
  //get lat and lon
  fetch(`http://127.0.0.1:8000/weather/${city}`)
    // Convert response string to json object
    .then(response => response.json())
    .then(response => {


      let temperature = response['temp'] - 273.15;
      let format_temp = temperature.toFixed(1);
      let clouds = response['description'];
      let pressure = response['pressure'];

      console.log(response)

      // Copy one element of response to our HTML paragraph
      document.getElementById("get_temp").innerHTML = format_temp + "°C";
      document.getElementById("icon").src = `https://openweathermap.org/img/wn/${response.weather[0].icon}@2x.png`;
      document.getElementById("myclouds").innerHTML = clouds.toUpperCase();
      document.getElementById("pressure").innerHTML = pressure+"hPa";
      console.log(response)

    })
    .catch(err => {
      // Display errors in console
      console.log(err);
    });
}



