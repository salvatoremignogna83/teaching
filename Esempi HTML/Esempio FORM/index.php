<?php ?>

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
        <title>Invio i dati</title>
    </head>

    <body>
        <h1> Raccolta dati </h1>
        <form action="ricevitore.php" method="post" name="datiUtenti">
        Nome :   <input type="text" name="nome" /></br>
        Cognome :   <input type="text" name="cognome" /></br>
        Età :    <input type="text" name="eta" /></br>
        Genere : <select name="genere">
                    <option value="uomo" selected="selected">uomo</option>
                    <option value="donna">donna</option>
                    <option></option>
                </select>
        </br>
        Suggerimenti :</br>
            <textarea name="testo" cols="40" rows="5"></textarea></br>
            <input type="submit" />
        </form>

    </body>
</html>