import axios from 'axios';//eh o hook que faz comunicação com a internet (http)
/**
 * hooks que permite a validação de interação com o usuário
 * NUNCA DUVIDE DA CAPACIDADE DO USUARIO
 * react é comum ver o zod
 */
import { useEffect, useState } from 'react';
import { useForm } from 'react-hook-form';//Hook determinado pela palavra (use) na frente
import { z } from 'zod';//zod é uma descrição de como eu validar, quais serial as regras
import { zodResolver } from '@hookform/resolvers/zod';//é o que liga o hook form com o zod
import { useNavigate } from 'react-router-dom';//permite navegar entre as páginas

const schemaCadTarefa = z.object({
    desc_tarefa: z.string()
        .min(10, 'Insira ao menos uma frase')
        .max(100, 'Insira uma descrição válida'),

    nome_setor: z.string()
        .min(1, 'Insira o nome do setor')
        .max(100, 'Máximo 100 caracteres')
        .regex(/^[A-Za-zÀ-ÿ\s]+$/, 'Digite apenas letras'),

    prioridade: z.enum(['baixa', 'media', 'alta'], {
        errorMap: () => ({ message: 'Prioridade inválida' })
    }),

    status: z.enum(['a fazer', 'fazendo', 'pronto'], {
        errorMap: () => ({ message: 'Status inválido' })
    }),

    usuario: z.number({
        required_error: "Selecione um usuário"
    }).int().positive("ID do usuário inválido"), // espera id do usuário
});

export function CadTarefa(){
    const [usuarios, setUsuarios] = useState([]);
    const navigate = useNavigate();

     const {
        register, //registra pra mim oq o usuario faz
        handleSubmit,//no momento em que ele der um submit (botao)
        formState: { errors },// no formulario, se der ruim guarda os errosna variavel errors
        reset
    } = useForm({
        resolver: zodResolver(schemaCadTarefa),//para validar eu chamo o resolver
        defaultValues: {
            status: 'a fazer'
        }
    });

    useEffect(() => {
        async function buscarUsuario() {
            try{
                const response = await axios.get('http://127.0.0.1:8000/usuario/') 
                setUsuarios(response.data);

            }catch(error){
                console.error("erro", error);
            }
        }
        buscarUsuario(); //chamando minha função para chamar usuarios
    }, [])

    async function obterDados(data) {
        console.log("dados da tarefa informado pelo usuario: ", data)

        try{
            await axios.post("http://127.0.0.1:8000/tarefa/", data);
            alert("Tarefa cadastrada com sucesso"); 
            reset(); ///limpo meu form
            navigate('/') //depois de cadastrar a tarefa, levo o usuario para o quadro
        } catch (error){
            alert("Erro no cadastro da tarefa. Verifique as informações")
            console.log("Erros", error)
            console.log(error.response.data)
        }
    }

    return(
        <form className='formularios' onSubmit={handleSubmit(obterDados)}>
            <h2> Cadastro de Tarefas </h2>

            <label>Nome do usuário </label>
            <select
                {...register('usuario', { valueAsNumber: true })}>
                    <option>Selecione o usuário </option>
                        {usuarios.map((user) => (
                            <option key={user.id} value={user.id}>
                                {user.nome}
                            </option>
                ))} 
            </select>
            {/* aqui eu vejo a variavel erros no campo nome e exibo a mensagem de erro para o usuario */}
            {errors.usuario && <p className= 'errors'>{errors.usuario.message}</p>}

            <label>Descrição: </label>
            <input 
            type="text" 
            {...register("desc_tarefa")} />
            {errors.descricao && <p className= 'errors'> {errors.descricao.message}</p>}

            <label>Nome do setor: </label>
            <input 
                type="text" 
                {...register("nome_setor")}
                placeholder='trabalho' 
            />
            {errors.nomeSetor && <p className= 'errors'> {errors.nomeSetor.message}</p>}

            <label>Prioridade: </label>
            <select {...register("prioridade")}>
                <option value=""> Selecione o nível de prioridade</option>
                <option value="baixa">Baixa</option>
                <option value="media">Media</option>
                <option value="alta">Alta</option>
            </select>
            {errors.prioridade && <p className= 'errors'> {errors.prioridade.message}</p>}

            <label>Status: </label>
            <select {...register("status")}>
                <option value=""> Selecione o status da tarefa</option>
                <option value="a fazer">Fazer</option>
                <option value="fazendo">Fazendo</option>
                <option value="pronto">Feito</option>
            </select>
            {errors.status && <p className= 'errors'> {errors.status.message}</p>}

            <button type='submit'>Cadastrar tarefa</button>

        </form>
    )
  
}