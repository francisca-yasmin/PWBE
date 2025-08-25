import { Link } from 'react-router-dom'

export function Navbar(){
    return(
        <nav className="barra">
            <ul>
                <Link to = '/cadUsusario'>
                    <li>Cadastro de Usuário</li>
                </Link>

                <Link to= '/cadTarefa'>
                    <li>Cadastro de Tarefas</li>
                </Link>

                <Link to='/'>
                    <li>Gerenciar Tarefas</li>
                </Link>
            </ul>
        </nav>
    );
}