import React, {useEffect, useState} from "react";
import axios from 'axios'; 

import { Coluna } from "./Coluna";

export function Quadro(){

    const [tarefas, setTarefas] = useState([]);

    //o effect é um hook que permite a redenrização de alguma coisa na tela
    //ele é po fofoqueiro que conta para todo mundo o que o state tá fazendo
    //comporto por parametros. script (algoritmo) e depois as dependencias
    useEffect(() => {
        const apiURL = 'http://127.0.0.1:8000/tarefa/';

        axios.get(apiURL)
        //then é quando dar certo
        .then(response => {setTarefas(response.data)
        })
        //catch se deu algum problema
        .catch(error => {
            console.error("Não due certo", error)
        });
    },[])

    //estou fazendo em variaveis o resultado de uma função de callback que produra tarefas com certo status
    const tarefasAfazer = tarefas.filter(tarefa => tarefa.status === 'a fazer');
    const tarefasFazendo = tarefas.filter(tarefa => tarefa.status === 'fazendo');
    const tarefasPronto = tarefas.filter(tarefa => tarefa.status === 'pronto');


    return(
        <>
            <main className="conteiner"> {/* chamo o nome do meu componenten utilizado no css utilizando o sass */}
                <h1> Meu quadro </h1>
                <Coluna titulo = "a fazer" tarefa={tarefasAfazer}/>
                <Coluna titulo = "fazendo" tarefa={tarefasFazendo}/>
                <Coluna titulo = "pronto" tarefa={tarefasPronto}/>
            </main>
        
        </>
    );
}