function fun_palavra(){
    let palavra = document.getElementById("palavra").value;
    let frase = document.getElementById("frase").value;
    var igual = frase.match(palavra);

    if (igual == null){
        window.alert("A frase não contem essa palavra")
    }
    else if ( igual != null) {
        window.alert("A frase contém a palavra " + palavra)
    }
}