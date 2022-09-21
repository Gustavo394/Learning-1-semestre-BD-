function calcularpoluicao(){
    let poluicao = document.getElementById("pol").value;
    
    if (poluicao >= 55){
        window.alert("Saudações, por motivos de seguração ao meio ambiente, solicitamos que todas as atividades de todas as empresas sejam suspensas imediatamente!")
    }
    else if (poluicao >= 45){
        window.alert("Saudações, por motivos de seguração ao meio ambiente, solicitamos que todas as atividades das empresas dos grupos 1 e 2 sejam suspensas imediatamente!")
    }
    else if (poluicao >= 30){
        window.alert("Saudações, por motivos de seguração ao meio ambiente solicitamos que todas as atividades das empresas do grupo 1 sejam suspensas imediatamente!")
    }
    else if (poluicao >= 27){
        window.alert("Índice de poluição elevado, caso necessário as empresas serão notificadas para suspender as atividades!")
    }
    else{
        window.alert("O índice de poluição se encontra dentro dos padroes!")
    }
}