


export function Tarefa({tarefa}){
    return(
        // configurar bonitinhos cluninhas
        <article>
            <h3 id={`tarefa: ${Tarefa.id}`}> {tarefa.descricao}</h3>
            {/* dl -> lista de detalhes == dd -> detalhe do detalhe */}
            <dl>
                <dt>Setor:</dt>
                <dd>{tarefa.setor}</dd>

                <dt>Prioridade:</dt>
                <dd>{tarefa.prioridade}</dd>
            </dl>

                <button>Editar</button>
                <button>Excluir</button>

            <form>
                <label>Status:</label>
                <select id={tarefa.id} name='status'>
                    <option value="">Selecione o status</option>
                    <option value="a fazer">A Fazer</option>
                    <option value="fazendo">Fazendo</option>
                    <option value="pronto">Pronto</option>
                </select>
                <button>Alterar status</button>
            </form>
        </article>

    );
}