
//poppover

const popoverTriggerList = document.querySelectorAll('[data-bs-toggle="popover"]')
const popoverList = [...popoverTriggerList].map(popoverTriggerEl => new bootstrap.Popover(popoverTriggerEl))


/////////////// CARRUSEL


$(window).on('load', function(){
            $('#slider').nivoSlider();
        });

//////////////////login///////////////////////////

function validateLoginForm() {
    var email = $('#login-correo').val();

    // Validar el formato del correo electrónico
    var emailFormat = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!email.match(emailFormat)) {
        alert("Por favor, ingrese un correo electrónico válido.");
        return false;
    }

    return true;
}
//////////////////registrar///////////////////////////

function validateRegistroForm() {
    var nombre = $('#registrar-nombre').val();
    var apellido = $('#registrar-apellido').val();
    var rut = $('#registrar-rut').val();
    var email = $('#registrar-correo').val();
    var confirmarEmail = $('#confirmar-correo').val();
    var contrasena = $('#registrar-contraseña').val();
    var confirmarContrasena = $('#confirmar-contraseña').val();

    // Verificar si al menos un campo está lleno
    if (nombre == "" || apellido == "" || rut == "" || email == "" || confirmarEmail == "" || contrasena == "" || confirmarContrasena == "") {
        alert("Debe completar todos los campos");
        return false;
    }

    // Validar que el nombre esté dentro del rango adecuado
    if (nombre.length <= 3 || nombre.length > 20) {
        alert("El nombre debe tener entre 3 y 20 caracteres.");
        return false;
    }

    // Validar el formato del correo electrónico
    var emailFormat = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (email && !email.match(emailFormat)) {
        alert("Por favor, ingrese un correo electrónico válido.");
        return false;
    }

    // Validar que los correos electrónicos coincidan
    if (email != confirmarEmail) {
        alert("Los correos electrónicos no coinciden.");
        return false;
    }

    // Validar que las contraseñas coincidan
    if (contrasena != confirmarContrasena) {
        alert("Las contraseñas no coinciden.");
        return false;
    }

    // Validar que el RUT solo tenga números y sea un número válido
    var rutFormat = /^\d+$/;
    if (rut && !rut.match(rutFormat)) {
        alert("Por favor, ingrese un RUT válido.");
        return false;
    }
	    // Validar la contraseña
	var contrasenaFormat = /^(?=.*[A-Z])(?=.*\d).{6,}$/;
	if (!contrasena.match(contrasenaFormat)) {
		alert("La contraseña debe tener al menos 6 caracteres, incluyendo una letra mayúscula y un número.");
		return false;
	}
    return true;
}	

//////////////////actualizar///////////////////////////

function validateUpdateForm() {
    var nombre = $('#nombreInput').val();
    var apellido = $('#apellidosInput').val();
    var email = $('#emailInput').val();
    var contrasena = $('#telefonoInput').val();
    var confirmarContrasena = $('#marcaInput').val();

    // Verificar si al menos un campo está lleno
    if (nombre == "" && apellido == "" && email == "" && contrasena == "" && confirmarContrasena == "") {
        alert("Al menos un campo debe estar lleno");
        return false;
    }

    // Validar que ambas contraseñas sean iguales
    if (contrasena !== confirmarContrasena) {
        alert("Las contraseñas no coinciden.");
        return false;
    }

    // Validar que si una contraseña está llena, la otra también debe estarlo
    if ((contrasena !== "" && confirmarContrasena === "") || (contrasena === "" && confirmarContrasena !== "")) {
        alert("Ambos campos de contraseña deben estar llenos.");
        return false;
    }

    // Validar los requisitos de la contraseña
    if (contrasena !== "" && !contrasena.match(/^(?=.*[A-Z])(?=.*\d).{6,}$/)) {
        alert("La contraseña debe tener al menos 6 caracteres, incluyendo una letra mayúscula y un número.");
        return false;
    }

    return true;
}

//////////////////recuperar///////////////////////////

function validateFormRecuperar() {
	var recuperar = $('#recuperar-correo').val();
	if (recuperar == "") {
		alert("El campo debe estar lleno");
		return false;
	}
	var emailFormat = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
	if (!recuperar.match(emailFormat) ) {
		alert("Por favor, ingrese un correo electrónico válido.");
		return false;
	}
	return true;
}
	
////////////////// contacto///////////////////////////	
	
		
function validateFormCotacto() {
	var name = $('#name').val();
	var email = $('#email').val();
	var phone = $('#phone').val();
	var message = $('#message').val();
	if (name == "" || email == "" || phone == "" || message == "") {
		alert("Todos los campos deben estar llenos");
		return false;
	}
	if (nombre.length >= 3 || nombre.length > 21) {
		alert("El nombre debe tener entre 3 y 20 caracteres.");
		return false;
	}
	var emailFormat = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
	if (!email.match(emailFormat) ) {
		alert("Por favor, ingrese un correo electrónico válido.");
		return false;
	}
	var phoneFormat = /^\d+$/;
	if (!phone.match(phoneFormat)) {
		alert("Por favor, ingrese un número de teléfono válido.");
		return false;
	}
	if (message.length > 100) {
        alert("El mensaje debe tener un máximo de 100 caracteres.");
        return false;
    }
	return true;
}

//////////////////reserva///////////////////////////	
/*
var select = document.getElementById("anioSelect");
    var year = new Date().getFullYear();
    var earliestYear = 1950;

    for(var i = year; i >= earliestYear; i--){
        var option = document.createElement("option");
        option.text = i;
        option.value = i;
        select.appendChild(option); 
    }
	*/
$(document).ready(function() {
    var $select = $("#anioSelect");
    var year = new Date().getFullYear();
    var earliestYear = 1950;
    var options = "";

    for(var i = year; i >= earliestYear; i--){
        options += `<option value="${i}">${i}</option>`;
    }

    $select.html(options);
});


	
function validateFormReserva() {
	var nombre = $("#nombreInput").val();
	var apellidos = $("#apellidosInput").val();
	var rut = $("#rutInput").val();
	var email = $("#emailInput").val();
	var telefono = $("#telefonoInput").val();
	var marca = $("#marcaInput").val();
	var anio = $("#anioSelect").val();
	

	if (nombre == "" || apellidos == "" || rut == "" || email == "" || telefono == "" || marca == "" || anio == "Seleccione año del vehiculo") {
		alert("Por favor, complete todos los campos del formulario.");
		return false;
	}

	// Validación de largo
	if (nombre.length <= 3 || nombre.length > 21) {
		alert("El nombre debe tener entre 3 y 20 caracteres.");
		return false;
	}

	if (apellidos.length <= 3 || apellidos.length > 21) {
		alert("El apellido debe tener entre 3 y 20 caracteres.");
		return false;
	}
	if ( rut.length > 11 || rut.length < 8) {
		alert("El rut debe tener entre 8 y 10 caracteres.");
		return false;
	}

	if (telefono.length < 9 || telefono.length > 12) {
		alert("El teléfono debe tener entre 9 y 12 caracteres.");
		return false;
	}
	
	// Validación de formato de correo electrónico
	var emailFormat = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
	if (!email.match(emailFormat) ) {
		alert("Por favor, ingrese un correo electrónico válido.");
		return false;
	}

	// Validación de formato de teléfono (solo dígitos)
	var phoneFormat = /^\d+$/;
	if (!telefono.match(phoneFormat)) {
		alert("Por favor, ingrese un número de teléfono válido.");
		return false;
	}

	// Validación de formato de RUT
	
	return true;

	


}

// API

	$(document).ready(function() {
		// Reemplaza 'your_api_key' con tu clave API de OpenWeatherMap
		var apiKey = 'a4a334d9aee54dc41211d403964ea7cc';
	
		// Define la ciudad para la que deseas obtener el clima
		var city = 'Viña del Mar';
	
		// Construye la URL para la API de OpenWeatherMap
		var apiUrl = 'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=' + apiKey;
	
		// Realiza una solicitud GET a la API de OpenWeatherMap
		$.get(apiUrl, function(response) {
			// Extrae la temperatura actual (en grados Kelvin)
			var temperatureInKelvin = response.main.temp;
	
			// Convierte la temperatura a Celsius
			var temperatureInCelsius = Math.round(temperatureInKelvin - 273.15);
	
			// Extrae la descripción del clima
			var weatherDescription = response.weather[0].description;
	
			// Actualiza los elementos HTML con la temperatura y la descripción del clima
			$('#temperature').text('Temperature: ' + temperatureInCelsius + '°C');
			$('#weather').text('Weather: ' + weatherDescription);
		});
	});
	
	
	
//////////////////barra de contacto///////////////////////////	
	var v = 48;
 	$(".legend").click(function(){
	if (v ==48){ 
	    v = 480;
		$("#wrapper-formulario").height(v);
	} 
	else{
		v = 48;
    	$("#wrapper-formulario").height(v);
	}});
	
	$("#onecontact").click(function(){
	if (v ==48){ 
	    v = 480;
		$("#wrapper-formulario").height(v);
	} 
	else{
		v = 48;
    	$("#wrapper-formulario").height(v);
	}}); 
//////////////////barra loging dropdown///////////////////////////
$(document).ready(function() {
	$(document).click(function(event) {
		var clickover = $(event.target);
		var _opened = $(".dropdown-toggle").hasClass("show");
		if (_opened === true && !clickover.closest('.dropdown').length) {
			$(".dropdown-toggle").dropdown('toggle');
		}
	});
});

// CARRITO 



	