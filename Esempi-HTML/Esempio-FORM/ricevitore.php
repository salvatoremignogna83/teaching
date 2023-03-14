<?php

    $nome= $_POST["nome"];
    $cognome = $_POST["cognome"];
    $eta= $_POST["eta"];
    $genere= $_POST["genere"];
    $testo = $_POST["testo"];

    if ($var3 == "uomo"){
        $articolo = "un" ;}
    else{
        $articolo = "una";}

    echo "Ciao $nome $cognome hai $eta anni, sei $articolo $genere e suggerisci: </br> $testo";

?>