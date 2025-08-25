import { Navbar } from "../components/Navbar";
import { Header } from "../components/Header";
import { Outlet } from 'react-router-dom'

export function Inicial(){
    return(
        <>
            <Navbar/>
            <Header/>
            <Outlet/>
        </>

    );
}