import axios from "axios";
import { useState } from "react";
import { useNavigate } from "react-router-dom";

export function Tarefa({ tarefa }){
    const [status, setStatus] = useState(tarefa.status || "");
    const navigate = useNavigate();

    //fazendo a exclusão de uma tarefa
    //async eh porque eu não sei extamente o tempo de resposta
    //função deve ter um nome que remeta a sua funcionalidade
    async function excluirTarefa(id) {

        if(confirm("Tem certeza que deseja excluir esta tarefa?")){
            try {
                await axios.delete(`http://127.0.0.1:8000/tarefa/${id}/`);
                alert("Tarefa excluida com sucesso.");
                window.location.reload(); //recarregar a pagina com a tarefa excluida -> refresh
            }catch(error){
                console.error("Erro ao excluir a tarefa, tente novamente", error);
                alert("Erro ao excluir a tarefa");
            }
        }
    }//fim da função
    
    async function alterarStatus() {
        try{
            await axios.patch(`http://127.0.0.1:8000/tarefa/${tarefa.id}/`, {
                status: status,
            });
            alert("Tarefa foi editada com sucesso");
            window.location.reload();
        }catch(error){
            console.error("Erro ao editar esta tarefa.", error);
            alert("Erros ao ediar a tarefa");
        }        
    }

    return(
        // configurar bonitinhos cluninhas
        <article className="tarefa">
            <h3 id={`tarefa: ${Tarefa.id}`}> {tarefa.descricao}</h3>
            {/* dl -> lista de detalhes == dd -> detalhe do detalhe */}
            <dl>
                <dt>Setor:</dt>
                <dd>{tarefa.setor}</dd>

                <dt>Prioridade:</dt>
                <dd>{tarefa.prioridade}</dd>
            </dl>

                <button onClick={()=> navigate(`/editarTarefa/${id}`)}>Editar</button>
                <button onClick={() => excluirTarefa(tarefa.id)}>Excluir</button>

            <form>
                <label>Status:</label>
                <select id={tarefa.id} name='status' value={status} onChange={(e) => setStatus(e.target.value)}>
                     {/* se houver mudança no campo de status isso é um evento que mudara
                     esse evento armazenado no state  */}
                    <option value="">Selecione o status</option>
                    <option value="a fazer">A Fazer</option>
                    <option value="fazendo">Fazendo</option>
                    <option value="pronto">Pronto</option>
                </select>
                <button onClick={alterarStatus}>Alterar status</button>
            </form>
        </article>

    );
}