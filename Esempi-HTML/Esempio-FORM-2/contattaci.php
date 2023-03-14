<?php

$password= $_POST["password"];
if ($password == "vivahtml"){
    echo "<h2> Password corretta! Grazie per averci contattato </h2>";
}else{
    echo "<h2> Password errata! siamo spiacenti ma non possiamo soddisfare la sua richiesta</h2>";
}

?>