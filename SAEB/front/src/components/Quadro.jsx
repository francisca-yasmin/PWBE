import { Coluna } from "./Coluna";

export function Quadro(){
    return(
        <>
            <main className="conteiner"> {/* chamo o nome do meu componenten utilizado no css utilizando o sass */}
                <h1> Meu quadro </h1>
                <Coluna/>
            </main>
        
        </>
    );
}