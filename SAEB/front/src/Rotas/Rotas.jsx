import { Routes, Route } from 'react-router-dom'
import { Inicial } from '../pages/Inicial';
import { Quadro } from '../components/Quadro';
import { CadUsuario } from '../pages/CadUsuario';
import { CadTarefa } from '../pages/CadTarefa';
import { EditarTarefa } from '../pages/EditarTarefa';

export function Rotas(){
    return(
        <Routes>
            <Route path='/' element={<Inicial/>}>
                <Route index element ={<Quadro/>}/>
                <Route path= '/cadUsusario' element={<CadUsuario/>}/>
                <Route path='/cadTarefa' element={<CadTarefa/>}/>
                <Route path='/editarTarefa/:id' element={<EditarTarefa/>}/>
            </Route>
        </Routes>
    );
}