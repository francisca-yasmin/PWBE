import axios from 'axios';
import { useForm } from 'react-hook-form';
import { z } from 'zod';
import { zodResolver } from '@hookform/resolvers/zod';

//validação de formulario
const schemaCadUsuario = z.object({
    nome: z.string()
        .min(1,' insira ao menos 1 caractere')
        .max(100, 'Insira no maximo 100 caracteres'),
    email: z.string()
        .min(1, 'insira seu email')
        .max(255, 'Insira um emial com até 255 caracteres')
        .email('Formato de email invalido'),
    
})

export function CadUsuario(){
    return(
        <form>
            <h2>Cadastro do Usuário</h2>

            <label>Nome:</label>
            <input type="text" placeholder='Nome do user' />

            <label>E-mail</label>
            <input type="email" placeholder='email@gmail.com' />

            <button type='submit'>Cadastrar</button>
        </form>
    );
}