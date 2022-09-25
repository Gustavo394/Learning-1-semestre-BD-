function fun_aumento(){
    var nome = document.getElementById("nome").value;
    var h_sal = document.getElementById("h_sal").value;
    var h_trab = document.getElementById("h_trab").value;
    var num_dep = document.getElementById("num_dep").value;

    if (nome, h_sal, h_trab, num_dep != ""){
        if (num_dep <=3){
            window.alert("Olá " + nome + ", por hora, você não tem direito a um aumento")
        }
        else if (num_dep > 3){
            h_s_t = h_sal*h_trab
            aumento = (((h_sal/100)*3)*num_dep)*h_trab
            total = h_s_t + aumento
            window.alert("Olá " + nome + ", você receberia " + h_s_t + " pelas horas trabalhadas\n"
            + "Você tem direito a um aumento de " + aumento + "\n"
            + "Portanto receberá " + total)
        }
    }
    else{
        window.alert("Preencha todos os campos!")
    }
}