import React, { useState, useEffect } from "react";
import axios from "axios";
import { Coluna } from "./Coluna";

export function Quadro () {
    const [tarefas, setTarefas] = useState([]);

    // o Effect é um hook que permite a renderização de alguma coisa na tela
    useEffect (() => {

        //construo uma variável com o endereço da API
        const apiURL = 'http://127.0.0.1:8000/tarefa/';

        //permite a chamada do endereço
        axios.get(apiURL)

            //se a resposta for positiva
            .then(response => {setTarefas(response.data)
            })

            //se der algum problema
            .catch(error => {
                console.error("Algo seu errado", error)
            });
    }, [])

    //armazenando em variáveis o resultado de uma função callback que procura tarefas com um certo status
    const tarefasAfazer = tarefas.filter(tarefa => tarefa.status === 'a fazer');
    const tarefasFazendo = tarefas.filter(tarefa => tarefa.status === 'fazendo');
    const tarefasPronto = tarefas.filter(tarefa => tarefa.status === 'pronto');

    return (

        <main className="conteiner">
            <h1>Minhas Tarefas</h1>

            <div className="colunas">
                <Coluna titulo = "a fazer" tarefas={tarefasAfazer}/>
                <Coluna titulo = "fazendo" tarefas={tarefasFazendo}/>
                <Coluna titulo = "pronto" tarefas={tarefasPronto}/>
            </div>
          
        </main>
        
        
    );

}