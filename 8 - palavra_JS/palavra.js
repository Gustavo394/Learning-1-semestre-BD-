function fun_palavra(){
    let palavra = document.getElementById("palavra").value;
    var ver = new RegExp(palavra.toLowerCase(),"g");
    let frase = document.getElementById("frase").value;
    frase = frase.toLowerCase();
    var num = (frase.match(ver)||[]).length;

    if (palavra, frase != ""){
        if (num == 0){
            window.alert("A palavra " + palavra + " não está presente na frase");
        }
        else if (num == 1){
            window.alert("A palavra " + palavra + " apareceu " + num + " vez na frase");
        }
        else if (num > 1){
            window.alert("A palavra " + palavra + " apareceu " + num + " vezes na frase");
        }
    }
    else{
        window.alert("Preencha todos os campos!");
    }
}