<?php
//get data from form  
$evento = $_POST['evento'];
$nombre = $_POST['nombre'];
$apellido = $_POST['apellidos'];
$fecha = $_POST['fechaReserva'];
$email= $_POST['email'];
$message= $_POST['message'];

$to = "luna.htz@mail.com";
$subject = "Reserva Web Salón";
$txt ="Evento = ". $evento . " \r\n Nombre = ". $nombre . " \r\n  Apellido = " . $apellido . " \r\n Fecha =" . $fecha . " \r\n  Email = " . $email . "\r\n Message =" . $message;
$headers = "From: noreply@bochasclub.com" . "\r\n" .
"CC: somebodyelse@example.com";
if($email!=NULL){
    mail($to,$subject,$txt,$headers);
}
//redirect
header("Location:gracias.html");
?>