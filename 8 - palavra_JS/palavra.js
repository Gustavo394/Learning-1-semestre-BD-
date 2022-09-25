function fun_palavra(){
    let palavra = document.getElementById("palavra").value;
    let frase = document.getElementById("frase").value;
    var igual = frase.match(palavra);

    if (palavra, frase != ""){
        if (igual == null){
            window.alert("A frase não contem essa palavra")
        }
        else if ( igual != null) {
            window.alert("A frase contém a palavra " + palavra)
        }
    }
    else{
        window.alert("Preencha todos os campos!")
    }
}