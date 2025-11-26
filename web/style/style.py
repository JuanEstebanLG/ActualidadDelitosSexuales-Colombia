def boxes(mayor, menor, mediana):
    return (
"""
<style>
.stats_container{
display: grid;
grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
gap: 16px;
margin: 10px 0 18px 0;
width: 100%;
}

.stat_box{
background: #2e3441;
border-radius: 16px;
border: 1px solid rgba(148,163,184,0.35);
padding: 16px 18px;
box-shadow: 0 12px 18px rgba(0,0,0,0.2);
display: flex;
flex-direction: column;
gap: 4px;
position: relative;
overflow: hidden;
transform: translateY(12px) scale(0.97);
opacity: 0.5;
animation: statsFloatIn 0.75s ease-out forwards;
}

.stat_box::before{
content: "";
position: absolute;
inset: -40%;
background:#101827;
opacity: 0.5;
pointer-events: none;
z-index: 0;
}

.stat_box:nth-child(1){
animation-delay: 0.08s;
}
.stat_box:nth-child(2){
animation-delay: 0.18s;
}
.stat_box:nth-child(3){
animation-delay: 0.28s;
}

.stat_title{
font-size: 0.85rem;
text-transform: uppercase;
letter-spacing: 0.09em;
color: #9CA3AF;
position: relative;
z-index: 1;
}

.stat_value{
font-size: 1.25rem;
font-weight: 700;
color: #F9FAFB;
margin-top: 2px;
position: relative;
z-index: 1;
}

.stat_value span{
font-weight: 400;
font-size: 0.9rem;
color: #E5E7EB;
}

.stat_hint{
font-size: 0.8rem;
color: #D1D5DB;
margin-top: 4px;
position: relative;
z-index: 1;
}

.stat_box_mayor .stat_value{
color: #F97373;
}

.stat_box_menor .stat_value{
color: #22D3EE;
}

.stat_box_mediana .stat_value{
color: #A5B4FC;
}

.stat_box:hover{
transform: translateY(0px) scale(1.01);
border-color: rgba(129,140,248,0.95);
transition:
transform 0.18s ease,
box-shadow 0.18s ease,
border-color 0.18s ease;
}

/* Animación de entrada */
@keyframes statsFloatIn{
from{
opacity: 0;
transform: translateY(18px) scale(0.96);
}
to{
opacity: 1;
transform: translateY(0) scale(1);
}

/* Responsivo suave */
@media (max-width: 600px){
.stat_box{
padding: 14px 14px;
border-radius: 14px;
}
}
}
</style>

<div class="stats_container">

<div class="stat_box stat_box_mayor">
<div class="stat_title">Más delitos reportados</div>
<div class="stat_value">""" + str(mayor) + """</div>
<div class="stat_hint">
Departamento con el número más alto de casos registrados en el periodo analizado.
</div>
</div>

<div class="stat_box stat_box_menor">
<div class="stat_title">Menos delitos reportados</div>
<div class="stat_value">""" + str(menor) + """</div>
<div class="stat_hint">
Departamento con el menor número de casos en términos absolutos dentro del dataset.
</div>
</div>

<div class="stat_box stat_box_mediana">
<div class="stat_title">Mediana de delitos</div>
<div class="stat_value">""" + str(mediana) + """</div>
<div class="stat_hint">
Punto medio de la distribución: la mitad de los departamentos reporta más casos y la otra mitad menos.
</div>
</div>

</div>
"""
    )


h3_boxes = """
<style>

.stats_container {
    display: flex;
    justify-content: space-evenly;
    align-items: center;
    flex-wrap: wrap;
    gap: 40px;
    margin-top: 25px;
    padding: 10px;
}

/* ===== Tarjetas ===== */
.h3_boxes {
    position: relative;
    background: #1f1f22;               
    color: #EAEAEA;
    text-align: center;
    font-family: "Segoe UI", Roboto, sans-serif;
    font-weight: 400;
    line-height: 1.4;
    border-radius: 14px;
    padding: 25px 45px;
    min-width: 240px;                  
    box-shadow: 0 2px 8px rgba(0,0,0,0.25);
    transition: all 0.35s ease;
    animation: fadeIn 1s ease-in-out;
    overflow: hidden;
    border: 1px solid rgba(255,255,255,0.06);
}

/* ===== Contenido ===== */
.h3_boxes strong {
    display: block;
    font-weight: 600;
    font-size: 1.1em;
    letter-spacing: 0.4px;
    color: #FFFFFF;
    position: relative;
    z-index: 1;
}

.h3_boxes span {
    display: block;
    margin-top: 6px;
    font-weight: 600;
    font-size: 1.35em;
    color: #A8D0E6;                    
    position: relative;
    z-index: 1;
}


/* ===== Animaciones ===== */

/* Línea de enfoque */
.h3_boxes::after {
    content: "";
    position: absolute;
    left: 50%;
    bottom: 0;
    transform: translateX(-50%) scaleX(0);
    width: 80%;
    height: 2px;
    background: linear-gradient(90deg, #5dade2, #a8d0e6);
    transition: transform 0.4s ease;
    transform-origin: center;
    opacity: 0.8;
}

/* Hover general */
.h3_boxes:hover {
    transform: translateY(-6px);
    box-shadow: 0 8px 25px rgba(0,0,0,0.45);
    border-color: rgba(168,208,230,0.2);
}

/* Hover animación línea */
.h3_boxes:hover::after {
    transform: translateX(-50%) scaleX(1);
}

/* Hover color del número */
.h3_boxes:hover span {
    color: #C2E3F5;
    transition: color 0.3s ease;
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(40px); }
    to { opacity: 1; transform: translateY(0); }
}

</style>

"""


hero_cards = """
    <div class="hero">
        <div class="hero-text">
            <h1>Informe Nacional sobre Delitos Sexuales en Colombia (2010–2025)</h1>
            <h2>Una mirada integral hacia la comprensión y prevención</h2>
            <p>
            Este informe presenta un análisis detallado de los delitos sexuales cometidos en Colombia
            durante los últimos quince años, utilizando datos oficiales y técnicas de análisis estadístico.
            Su propósito es visibilizar la magnitud de esta problemática y ofrecer insumos para la toma
            de decisiones orientadas a la prevención y la atención de las víctimas.
            </p>
            <br>
            <p>
            En el contexto colombiano, los delitos sexuales representan un fenómeno complejo que impacta
            profundamente la estructura social y el bienestar de las comunidades. La persistencia de estos
            casos exige una reflexión colectiva sobre las políticas de educación, justicia y equidad de género,
            así como una revisión constante de las estrategias institucionales de protección y denuncia.
            </p>
        </div><div class="hero-side">
            <h3>¿Por qué este estudio es importante?</h3>
            <p>
            Comprender las tendencias de los delitos sexuales permite fortalecer las políticas públicas
            y enfocar esfuerzos en la protección de las víctimas, garantizando una Colombia más segura
            y consciente del valor de la integridad y la dignidad humana.
            </p>
        </div>
    </div>
    """

close_menu = """
    <style>
    [data-testid="stSidebarNav"] {display: none;}
    </style>
"""

home_styles = """
<style>

.stApp {
    background-color: #f4f4f4;
    background-image: url("https://github.com/JuanEstebanLG/ActualidadDelitosSexuales-Colombia/blob/Main/resources/images/foto_inicio.jpg?raw=true");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}


.hero {
    display: grid;
    grid-template-columns: 1.5fr 1fr;
    gap: 2rem;
    align-items: center;
    margin: 4rem auto;
    padding: 3rem 4rem;
    max-width: 1100px;
    background: rgba(255, 255, 255, 0.92);
    border-radius: 25px;
    box-shadow: 0 4px 25px rgba(0, 0, 0, 0.1);
    animation: fadeIn 1.2s ease-in-out;
}


.hero-text h1 {
    color: #0B2948;
    font-size: 2rem;
    font-weight: 800;
    margin-bottom: 0.5rem;
}

.hero-text h2 {
    color: #1b4f72;
    font-size: 1.3rem;
    margin-bottom: 1.5rem;
    font-weight: 600;
}

.hero-text p {
    color: #333;
    line-height: 1.6;
    font-size: 1rem;
    text-align: justify
}

/* Tarjeta lateral */
.hero-side {
    background: #0B2948;
    color: #fff;
    padding: 2rem;
    border-radius: 20px;
    box-shadow: 0 4px 20px rgba(11, 41, 72, 0.2);
    transform: translateY(0);
    transition: all 0.4s ease;
    text-align: justify
}

.hero-side:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 30px rgba(11, 41, 72, 0.3);
}

.hero-side h3 {
    font-size: 1.2rem;
    font-weight: 700;
    margin-bottom: 1rem;
    color: #f1f1f1;
}

.hero-side p {
    font-size: 0.95rem;
    line-height: 1.5;
}


@keyframes fadeIn {
    from { opacity: 0; transform: translateY(40px); }
    to { opacity: 1; transform: translateY(0); }
}
</style>
"""

info_team = """
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
    <style>
    body {
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
    }
    /* GRID DEL EQUIPO */
    .team-grid {
        display: flex;
        justify-content: center;
        gap: 40px;
        flex-wrap: wrap;
        margin-top: 40px;
    }
    /* TARJETAS */
    .card {
        width: 320px;
        padding: 25px;
        border-radius: 25px;
        backdrop-filter: blur(14px) saturate(150%);
        background: rgba(255, 255, 255, 0.9);
        border: 1px solid rgba(255, 255, 255, 0.25);
        box-shadow: 0 12px 36px rgba(0, 0, 0, 0.20);
        text-align: center;
        transition: all 0.35s ease;
    }
    .card:hover {
        transform: translateY(-12px) scale(1.03);
        box-shadow: 0 20px 45px rgba(0, 0, 0, 0.30);
    }
    /* FOTOS */
    .card img {
        max-width: 160px;
        max-height: 160px;
        width: 100%;
        height: auto;
        object-fit: contain;
        border-radius: 100%;
        margin-bottom: 15px;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.25);
    }
    /* NOMBRES */
    .card h3 {
        font-size: 22px;
        margin-bottom: 8px;
        color: #111;
    }
    /* DESCRIPCIÓN */
    .card p {
        font-size: 15px;
        text-align: justify;
        line-height: 1.55;
        color: #333;
        margin-bottom: 14px;
    }
    /* ICONOS DE CONTACTO */
    .contact-icons a {
        margin: 0px 10px;
        font-size: 22px;
        color: #007aff;
        transition: 0.25s ease;
    }
    .contact-icons a:hover {
        color: #0051a8;
        transform: scale(1.15);
    }
    </style>
    <div class="team-grid">
        <!-- Esteban -->
        <div class="card">
            <img src="https://github.com/JuanEstebanLG/ActualidadDelitosSexuales-Colombia/blob/Main/resources/images/Esteban.jpg?raw=true" alt="Foto de Perfil, Juan Esteban López García">
            <h3>Juan Esteban López García</h3>
            <p>
                Desarrollador de software enfocado en backend, con experiencia creando APIs y servicios robustos apoyado en el ecosistema de Spring y bases de datos relacionales. Trabajo con Java, Kotlin y Python, control de versiones con Git/GitHub y despliegue con Docker. Conocimientos en análisis de datos con herramientas como Pandas/Power BI para generar insights accionables.
            </p>
            <div class="contact-icons">
                <a href="https://github.com/JuanEstebanLG" target="_blank"><i class="fa-brands fa-github"></i></a>
                <a href="https://www.linkedin.com/in/jlesteban3/" target="_blank"><i class="fa-brands fa-linkedin"></i></a>
            </div>
        </div>
        <!-- Miguel -->
        <div class="card">
            <img src="https://github.com/JuanEstebanLG/ActualidadDelitosSexuales-Colombia/blob/Main/resources/images/miguel.jpg?raw=true" alt="Foto 2">
            <h3>Miguel Angel Cuervo Espinosa</h3>
            <p>
                Analista de datos con formación en ingeniería y ciencias biológicas. Con experiencia en Python, Power BI y estadística para procesar, limpiar y visualizar datos complejos. 
                Mediante análisis, automatizaciones y reportes para la toma de decisiones y proyectos de investigación aplicada.
            </p>
            <div class="contact-icons">
                <a href="https://github.com/milcuervo" target="_blank"><i class="fa-brands fa-github"></i></a>
                <a href="https://www.linkedin.com/in/miguelcuervoe/" target="_blank"><i class="fa-brands fa-linkedin"></i></a>
            </div>
        </div>
        <!-- Camilo -->
        <div class="card">
            <img src="https://github.com/JuanEstebanLG/ActualidadDelitosSexuales-Colombia/blob/Main/resources/images/Juan_Camilo.jpeg?raw=true" alt="Foto 3">
            <h3>Juan Camilo Loaiza</h3>
            <p>
                Administrador financiero con 15 años de experiencia como auditor en diversas empresas, 
                especializado en fortalecer controles internos, mejorar procesos y asegurar la calidad de la información financiera.
            </p>
            <div class="contact-icons">
                <a href="https://github.com/TU_USUARIO" target="_blank"><i class="fa-brands fa-github"></i></a>
                <a href="https://www.linkedin.com/in/juancamilo/" target="_blank"><i class="fa-brands fa-linkedin"></i></a>
            </div>
        </div>
    </div>
    """
columna_izquierda_estilo = """
            <div style="
                color:white;
                background-color:rgb(65 76 101);
                text-align: center;
                border: 1px solid #1C1C1C;
                border-radius: 10px;
                padding: 10px 5px;
                margin-bottom: 15px;
                box-shadow: 0px 3px 8px rgba(0,0,0,0.2);
            ">
                <h3 style="margin: 0;">📑 DataFrame de Delitos Sexuales en Colombia (2025)</h3>
            </div>
            """




main_estilo = """
<style>
:root {
    --bg-dark: #0E1117;
    --bg-card: #23272E;
    --bg-hero: #111827;
    --accent: #6366F1;
    --accent-soft: rgba(99, 102, 241, 0.18);
    --text-main: #E5E7EB;
    --text-muted: #9CA3AF;
}

/* Scroll suave en toda la página */
html {
    scroll-behavior: smooth;
}

/* Fondo general oscuro (opcional, si tu app ya lo maneja puedes omitir esto) */
body {
    background-color: var(--bg-dark);
    color: var(--text-main);
}

/* Contenedor principal de la primera impresión */
.first-impression-wrapper {
    min-height: 100vh;
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 4rem 1.5rem;
    box-sizing: border-box;
    background:
        radial-gradient(circle at top left, #1F2937 0, #020617 45%, #020617 100%);
    color: var(--text-main);
    position: relative;
    overflow: hidden;
    border-radius: 0 0 32px 32px;
    box-shadow: 0 24px 80px rgba(0, 0, 0, 0.9);
    margin-bottom: 2rem;
    border-bottom: 1px solid rgba(148, 163, 184, 0.25);
}

/* Capa de “brillo” suave, ajustada a tema oscuro */
.first-impression-glow {
    position: absolute;
    inset: -20%;
    background:
        radial-gradient(circle at 10% 0%, rgba(99, 102, 241, 0.35), transparent 55%),
        radial-gradient(circle at 90% 100%, rgba(56, 189, 248, 0.30), transparent 55%);
    opacity: 0.65;
    pointer-events: none;
}

/* Contenido interno con grid */
.first-impression-content {
    position: relative;
    max-width: 1100px;
    width: 100%;
    display: grid;
    grid-template-columns: minmax(0, 2.1fr) minmax(0, 1.4fr);
    gap: 3rem;
    align-items: center;
    z-index: 1;
}

/* Bloque de texto principal */
.first-impression-text {
    animation: fadeInUp 0.8s ease forwards;
    opacity: 0;
}

.first-impression-eyebrow {
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
    padding: 0.25rem 0.8rem;
    border-radius: 999px;
    background: rgba(15, 23, 42, 0.7);
    border: 1px solid rgba(148, 163, 184, 0.6);
    font-size: 0.75rem;
    text-transform: uppercase;
    letter-spacing: 0.14em;
    color: var(--text-muted);
    margin-bottom: 0.9rem;
}

.first-impression-eyebrow-dot {
    width: 8px;
    height: 8px;
    border-radius: 999px;
    background: var(--accent);
    box-shadow: 0 0 0 6px rgba(99, 102, 241, 0.4);
}

.first-impression-title {
    font-size: clamp(2.3rem, 3.5vw, 3.1rem);
    line-height: 1.08;
    font-weight: 800;
    letter-spacing: -0.04em;
    margin-bottom: 1rem;
    color: #F9FAFB;
}

.first-impression-highlight {
    background: linear-gradient(135deg, #6366F1, #22D3EE);
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
}

.first-impression-subtitle {
    font-size: 1rem;
    line-height: 1.65;
    color: var(--text-muted);
    max-width: 34rem;
}

/* Chips de contexto */
.first-impression-chips {
    display: flex;
    flex-wrap: wrap;
    gap: 0.6rem;
    margin-top: 1.4rem;
}

.first-impression-chip {
    padding: 0.35rem 0.85rem;
    border-radius: 999px;
    font-size: 0.78rem;
    border: 1px solid rgba(148, 163, 184, 0.7);
    background: rgba(15, 23, 42, 0.85);
    backdrop-filter: blur(12px);
    color: #E5E7EB;
}

/* CTA principal */
.first-impression-actions {
    display: flex;
    flex-wrap: wrap;
    gap: 0.85rem;
    margin-top: 1.9rem;
}

.first-impression-cta-main {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0.85rem 1.6rem;
    border-radius: 999px;
    border: none;
    text-decoration: none;
    font-weight: 600;
    font-size: 0.95rem;
    background: linear-gradient(135deg, var(--accent), #4F46E5);
    color: white;
    box-shadow: 0 18px 45px rgba(0, 0, 0, 0.8);
    cursor: pointer;
    transition:
        transform 0.2s ease,
        box-shadow 0.2s ease,
        background 0.3s ease;
}

.first-impression-cta-main span {
color: white;}

.first-impression-cta-main span.icon {
    font-size: 1.1rem;
    transform: translateY(1px);
}

.first-impression-cta-main:hover {
    transform: translateY(-2px);
    box-shadow: 0 22px 55px rgba(0, 0, 0, 0.95);
    background: linear-gradient(135deg, #4F46E5, #22D3EE);
}

.first-impression-cta-secondary {
    font-size: 0.88rem;
    display: inline-flex;
    align-items: center;
    gap: 0.45rem;
    padding: 0.7rem 1.2rem;
    border-radius: 999px;
    border: 1px solid rgba(148, 163, 184, 0.7);
    background: rgba(15, 23, 42, 0.85);
    color: var(--text-muted);
    text-decoration: none;
    cursor: pointer;
    backdrop-filter: blur(10px);
    transition:
        background 0.2s ease,
        border-color 0.2s ease,
        transform 0.2s ease;
}

.first-impression-cta-secondary:hover {
    background: rgba(31, 41, 55, 0.95);
    border-color: rgba(148, 163, 184, 1);
    transform: translateY(-1px);
}

/* Panel derecho tipo “card de resumen” */
.first-impression-panel {
    background: rgba(17, 24, 39, 0.95);
    border-radius: 24px;
    padding: 1.4rem 1.5rem 1.5rem;
    box-shadow:
        0 18px 40px rgba(0, 0, 0, 0.95),
        0 0 0 1px rgba(31, 41, 55, 0.9);
    backdrop-filter: blur(18px);
    animation: fadeInRight 0.9s ease forwards;
    opacity: 0;
}

.first-impression-panel-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 0.9rem;
}

.first-impression-panel-title {
    font-size: 0.85rem;
    text-transform: uppercase;
    letter-spacing: 0.16em;
    color: var(--text-muted);
}

.first-impression-panel-tag {
    font-size: 0.72rem;
    padding: 0.25rem 0.6rem;
    border-radius: 999px;
    background: var(--accent-soft);
    color: #E0F2FE;
    font-weight: 600;
}

.first-impression-panel-metric {
    margin-top: 0.4rem;
    margin-bottom: 0.85rem;
}

.first-impression-panel-metric-label {
    font-size: 0.78rem;
    color: var(--text-muted);
    margin-bottom: 0.1rem;
}

.first-impression-panel-metric-value {
    font-size: 1.9rem;
    font-weight: 700;
    letter-spacing: -0.04em;
    color: #F9FAFB;
}

.first-impression-panel-metric-delta {
    font-size: 0.8rem;
    display: inline-flex;
    align-items: center;
    gap: 0.25rem;
    margin-top: 0.25rem;
    color: #dc143c;
}

.first-impression-badge-row {
    display: flex;
    flex-wrap: wrap;
    gap: 0.45rem;
    margin: 0.9rem 0 1rem;
}

.first-impression-badge {
    font-size: 0.72rem;
    padding: 0.25rem 0.55rem;
    border-radius: 999px;
    background: rgba(31, 41, 55, 0.95);
    color: #E5E7EB;
}

/* Pie del panel */
.first-impression-panel-footer {
    display: flex;
    align-items: center;
    gap: 0.6rem;
    padding-top: 0.8rem;
    border-top: 1px dashed rgba(75, 85, 99, 0.9);
}

.first-impression-panel-dot {
    width: 9px;
    height: 9px;
    border-radius: 999px;
    background: #16A34A;
    box-shadow: 0 0 0 4px rgba(22, 163, 74, 0.5);
}

.first-impression-panel-footer-text {
    font-size: 0.78rem;
    color: var(--text-muted);
}

/* Indicador de scroll hacia abajo */
.first-impression-scroll-indicator {
    position: absolute;
    bottom: 1.4rem;
    left: 50%;
    transform: translateX(-50%);
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 0.35rem;
    font-size: 0.72rem;
    letter-spacing: 0.16em;
    text-transform: uppercase;
    color: #9CA3AF;
    opacity: 0.9;
}

.first-impression-scroll-line {
    width: 1px;
    height: 36px;
    border-radius: 999px;
    background: linear-gradient(to bottom, rgba(148, 163, 184, 0.3), var(--accent));
    animation: scrollPulse 1.7s ease-in-out infinite;
}

/* Animaciones */
@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateY(16px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@keyframes fadeInRight {
    from {
        opacity: 0;
        transform: translateX(16px);
    }
    to {
        opacity: 1;
        transform: translateX(0);
    }
}

@keyframes scrollPulse {
    0% {
        transform: translateY(0);
        opacity: 0.5;
    }
    50% {
        transform: translateY(8px);
        opacity: 1;
    }
    100% {
        transform: translateY(0);
        opacity: 0.5;
    }
}

/* Responsivo */
@media (max-width: 900px) {
    .first-impression-wrapper {
        padding: 3.5rem 1.25rem 3rem;
        border-radius: 0 0 24px 24px;
    }

    .first-impression-content {
        grid-template-columns: 1fr;
        gap: 2.4rem;
    }

    .first-impression-panel {
        order: -1;
    }

    .first-impression-subtitle {
        max-width: 100%;
    }
}
</style>

<section class="first-impression-wrapper" id="first-impression">
<div class="first-impression-glow"></div>

<div class="first-impression-content">
<div class="first-impression-text">
<div class="first-impression-eyebrow">
<span class="first-impression-eyebrow-dot"></span>
<span>Visión general del informe</span>
</div>

<h1 class="first-impression-title">
Análisis crítico de los
<span class="first-impression-highlight">delitos sexuales en Colombia</span>
hasta 2025.
</h1>

<p class="first-impression-subtitle">
Una plataforma interactiva que transforma datos oficiales en evidencia clara para la
toma de decisiones, el diseño de políticas públicas y la protección de las víctimas.
</p>

<div class="first-impression-chips">
<span class="first-impression-chip">Cobertura nacional 2010–2025</span>
<span class="first-impression-chip">Análisis por departamento y municipio</span>
<span class="first-impression-chip">Enfoque en violencia contra la mujer</span>
</div>

<div class="first-impression-actions">
<a href="#contenido-principal" class="first-impression-cta-main">
<span>Explorar el informe</span>
<span class="icon">↓</span>
</a>
<a href="#contenido-principal" class="first-impression-cta-secondary">
<span>Ver métricas clave</span>
</a>
</div>
</div>

<aside class="first-impression-panel">
<div class="first-impression-panel-header">
<span class="first-impression-panel-title">Vista rápida</span>
<span class="first-impression-panel-tag">Actualizado 2025</span>
</div>

<div class="first-impression-panel-metric">
<div class="first-impression-panel-metric-label">
Casos registrados (Mayo 2025)
</div>
<div class="first-impression-panel-metric-value">
9&nbsp;587
</div>
<div class="first-impression-panel-metric-delta">
<span>▼ -62.1%</span>
<span>vs. 2024</span>
</div>
</div>

<div class="first-impression-badge-row">
<span class="first-impression-badge">Distribución por edad y género</span>
<span class="first-impression-badge">Comparación interanual</span>
<span class="first-impression-badge">Mapas y visualizaciones interactivas</span>
</div>

<div class="first-impression-panel-footer">
<span class="first-impression-panel-dot"></span>
<span class="first-impression-panel-footer-text">
Los valores mostrados son demostrativos. Las cifras reales se cargan desde el dataset oficial.
</span>
</div>
</aside>
</div>

<div class="first-impression-scroll-indicator">
<span>Desplázate</span>
<div class="first-impression-scroll-line"></div>
</div>
</section>

<div id="contenido-principal"></div>
"""





derechos = """
            <div style="text-align:center; margin-top:10px; color: #555;">
                Fuente: <a href="https://www.policia.gov.co/" target="_blank">
                <b>Policía Nacional de Colombia</b></a>
            </div>
            """


descripcion_estilo = """
            <div class="descripcion-hero">
                <h3 style="color:white; text-align:center;">🗺️ Ánalisis Exploratorio</h3>
                <p style="text-align:justify; color:white;">
                El anterior dataframe presenta una muestra representativa de los reportes
                de delitos sexuales ocurridos en Colombia hasta el año 2025. 
                La información muestra Departamento, Municipio, Arma usada, Fecha del Hecho, entre otros datos relevantes.
                <br>
                <br>
                El análisis, gráficas, mapas y demas visualizaciones posteriores se basan en este conjunto de datos, es importante que esto
                se tenga en cuenta a la hora de interpretar los resultados, por ejemplo, abajo se encuentra la gráfica de barras correspondiente a la distribución de delitos por departamento
                </p>
            </div>
            <style>
            .descripcion-hero{
                background: #2e3441;
                border: 1px solid #1C1C1C;
                border-radius: 10px;
                padding: 20px;
                box-shadow: 0px 3px 8px rgba(0,0,0,0.15);
                animation: fadeIn 1s ease-in-out;
            }

            @keyframes fadeIn {
            from { opacity: 0; transform: translateY(40px); }
            to { opacity: 1; transform: translateY(0);}
            }
        
        </style>
        """


############################# USO DE ARMAS #############################

componente_armas = """
<style>

.armas-card {
background: linear-gradient(135deg, rgba(248, 113, 113, 0.22), rgba(255, 255, 255, 0.02));
border: 1px solid rgba(248, 113, 113, 0.70);
padding: 28px;
border-radius: 18px;
color: #e5e7eb;
font-family: 'Segoe UI', sans-serif;
backdrop-filter: blur(4px);
animation: armasFade 1.2s ease forwards;
opacity: 0;
transform: translateY(20px);
transition: transform .4s ease, box-shadow .4s ease;
}
.armas-card:hover {
transform: translateY(4px);
box-shadow: 0 8px 22px rgba(248, 113, 113, 0.40);
}

.armas-title {
font-size: 1.8rem;
font-weight: 700;
color: #f9fafb;
}

.armas-line {
width: 70px;
height: 3px;
background: linear-gradient(90deg, #fee2e2, #f97373, #ef4444);
border-radius: 20px;
margin: 8px 0 22px 0;
animation: expandLine 1.4s ease-out forwards;
transform-origin: left;
opacity: 0;
}

.armas-text {
font-size: 1.04rem;
line-height: 1.65;
color: #e5e7eb;
text-align: justify;
}

@keyframes armasFade {
to { opacity:1; transform: translateY(0); }
}

@keyframes expandLine {
0% { transform: scaleX(0); opacity: 0; }
100% { transform: scaleX(1); opacity: 1; }
}

</style>

<div class="armas-card">
<div class="armas-title">Uso de Armas</div>
<div class="armas-line"></div>

<div class="armas-text">
El análisis del uso de armas en delitos sexuales permite comprender las dinámicas de coerción y 
poder presentes en estos casos. La comparación entre armas más utilizadas y aquellas secundarias 
revela patrones importantes sobre los métodos empleados para intimidar o someter a las víctimas.
<br><br>
Esta información es esencial para fortalecer medidas de prevención, ajustar protocolos de seguridad 
y orientar políticas públicas que reduzcan los factores de riesgo asociados al uso de armas 
en contextos de violencia sexual.
</div>
</div>
"""


############################# GRUPO ETARIO MÁS AFECTADO #############################

componente_edad = """
<style>

.edad-card {
background: linear-gradient(135deg, rgba(252, 211, 77, 0.22), rgba(255, 255, 255, 0.02));
border: 1px solid rgba(252, 211, 77, 0.70);
padding: 28px;
border-radius: 18px;
color: #e5e7eb;
font-family: 'Segoe UI', sans-serif;
backdrop-filter: blur(4px);
animation: edadFade 1.2s ease forwards;
opacity: 0;
transform: translateY(20px);
transition: transform .4s ease, box-shadow .4s ease;
}
.edad-card:hover {
transform: translateY(4px);
box-shadow: 0 8px 22px rgba(252, 211, 77, 0.40);
}

.edad-title {
font-size: 1.8rem;
font-weight: 700;
color: #f9fafb;
}

.edad-line {
width: 70px;
height: 3px;
background: linear-gradient(90deg, #fef9c3, #fde68a, #facc15);
border-radius: 20px;
margin: 8px 0 22px 0;
animation: expandLine 1.4s ease-out forwards;
transform-origin: left;
opacity: 0;
}

.edad-text {
font-size: 1.04rem;
line-height: 1.65;
text-align: justify;
color: #e5e7eb;
}

@keyframes edadFade {
to { opacity:1; transform: translateY(0); }
}

@keyframes expandLine {
0% { transform: scaleX(0); opacity: 0; }
100% { transform: scaleX(1); opacity: 1; }
}

</style>

<div class="edad-card">
<div class="edad-title">Grupo de Edad Más Afectado</div>
<div class="edad-line"></div>

<div class="edad-text">
La distribución de los delitos sexuales por edad evidencia qué grupos poblacionales se encuentran en 
mayor situación de vulnerabilidad. Esta información permite identificar si niñas, niños, adolescentes, 
personas adultas o mayores concentran la mayor carga de victimización.
<br><br>
Analizar estos rangos etarios es crucial para comprender tendencias demográficas críticas y 
desarrollar programas de acompañamiento, protección y prevención ajustados a cada etapa del ciclo de vida.
</div>
</div>
"""


############################# MAPA DE DELITOS SEXUALES EN COLOMBIA #############################

componente_mapa = """
<style>

.mapa-card {
background: linear-gradient(135deg, rgba(74, 222, 128, 0.22), rgba(255, 255, 255, 0.02));
border: 1px solid rgba(74, 222, 128, 0.70);
padding: 28px;
border-radius: 18px;
color: #e5e7eb;
font-family: 'Segoe UI', sans-serif;
backdrop-filter: blur(4px);
animation: mapaFade 1.2s ease forwards;
opacity: 0;
transform: translateY(20px);
transition: transform .4s ease, box-shadow .4s ease;
}
.mapa-card:hover {
transform: translateY(4px);
box-shadow: 0 8px 22px rgba(74, 222, 128, 0.40);
}

.mapa-title {
font-size: 1.8rem;
font-weight: 700;
color: #f9fafb;
}

.mapa-line {
width: 70px;
height: 3px;
background: linear-gradient(90deg, #dcfce7, #4ade80, #16a34a);
border-radius: 20px;
margin: 8px 0 22px 0;
animation: expandLine 1.4s ease-out forwards;
transform-origin: left;
opacity: 0;
}

.mapa-text {
font-size: 1.04rem;
line-height: 1.65;
text-align: justify;
color: #e5e7eb;
}

@keyframes mapaFade {
to { opacity:1; transform: translateY(0); }
}

@keyframes expandLine {
0% { transform: scaleX(0); opacity: 0; }
100% { transform: scaleX(1); opacity: 1; }
}

</style>

<div class="mapa-card">
<div class="mapa-title">Mapa de Delitos Sexuales en Colombia</div>
<div class="mapa-line"></div>

<div class="mapa-text">
La distribución geográfica de los delitos sexuales permite identificar zonas críticas donde la 
incidencia es mayor y donde la presencia institucional debe ser reforzada. Los departamentos con 
mayor intensidad en tonalidades más marcadas indican una carga significativa de casos reportados.
<br><br>
Esta lectura espacial facilita entender cómo factores territoriales, sociales y económicos influyen 
en la ocurrencia de estos delitos, permitiendo orientar estrategias diferenciales basadas en la 
realidad de cada región del país.
</div>
</div>
"""


############################# DELITOS SEXUALES POR GÉNERO #############################

componente_genero = """
<style>

.genero-card {
background: linear-gradient(135deg, rgba(96, 165, 250, 0.22), rgba(255, 255, 255, 0.02));
border: 1px solid rgba(96, 165, 250, 0.70);
padding: 28px;
border-radius: 18px;
color: #e5e7eb;
font-family: 'Segoe UI', sans-serif;
backdrop-filter: blur(4px);
animation: generoFade 1.2s ease forwards;
opacity: 0;
transform: translateY(20px);
transition: transform .4s ease, box-shadow .4s ease;
}
.genero-card:hover {
transform: translateY(4px);
box-shadow: 0 8px 22px rgba(96, 165, 250, 0.40);
}

.genero-title {
font-size: 1.8rem;
font-weight: 700;
color: #f9fafb;
}

.genero-line {
width: 70px;
height: 3px;
background: linear-gradient(90deg, #dbeafe, #60a5fa, #2563eb);
border-radius: 20px;
margin: 8px 0 22px 0;
animation: expandLine 1.4s ease-out forwards;
transform-origin: left;
opacity: 0;
}

.genero-text {
font-size: 1.04rem;
line-height: 1.65;
text-align: justify;
color: #e5e7eb;
}

@keyframes generoFade {
to { opacity:1; transform: translateY(0); }
}

@keyframes expandLine {
0% { transform: scaleX(0); opacity: 0; }
100% { transform: scaleX(1); opacity: 1; }
}

</style>

<div class="genero-card">
<div class="genero-title">Delitos Sexuales por Género</div>
<div class="genero-line"></div>

<div class="genero-text">
La distribución de los delitos sexuales según el género de las víctimas revela patrones profundos 
de desigualdad y vulnerabilidad. Las cifras permiten identificar qué géneros soportan la mayor 
proporción de casos, así como posibles variaciones y brechas en la victimización.
<br><br>
Comprender esta distribución es fundamental para visibilizar realidades que suelen permanecer 
ocultas y para orientar estrategias efectivas de prevención, atención integral y construcción 
de políticas públicas con un enfoque de género que responda a las necesidades reales de cada población.
</div>
</div>
"""


############################## EXPLICACION METRICAS ##############################
metric_explanation = """<style>
.metric-info-container {
    margin-top: 10px;
    margin-bottom: 10px;
}

.metric-info-box {
    background: linear-gradient(145deg, #252A34, #313746); /* un poco más clara que el body */
    color: #F3F3F3;
    padding: 16px 20px;
    border-radius: 12px;
    border: 1px solid rgba(255, 255, 255, 0.04);
    box-shadow: 0 14px 32px rgba(0, 0, 0, 0.45);
    font-size: 0.95rem;
    line-height: 1.5;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    animation: metricFadeIn 0.6s ease-out forwards;
    transform: translateY(8px);
    opacity: 0;
    transition: transform 0.8s ease, box-shadow 0.25s ease, border-color 0.25s ease;
    border-left: 4px solid #5BC0DE; 
}

.metric-info-box:hover {
    transform: translateY(4px);
    box-shadow: 0 18px 40px rgba(0, 0, 0, 0.55);
    border-left-color: #72D6F0;
}

@keyframes metricFadeIn {
    from {
        opacity: 0;
        transform: translateY(12px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}
</style>

<div class="metric-info-container">
    <div class="metric-info-box">
        Los valores positivos en las anteriores métricas indican un aumento en los casos reportados en comparación con el año anterior; por otro lado, los valores negativos indican una disminución de los casos reportados. Estos resultados permiten identificar de manera rápida si la situación presenta una tendencia al alza o a la baja respecto al periodo previo. La correcta interpretación de estos signos es fundamental para comprender la evolución de los casos y apoyar el análisis de la información presentada.
    </div>
</div>
"""
############################## VIOLENCIA DE GENERO, PANORAMA FEMENINO ##############################
violencia_genero = """
<style>
.violencia-wrapper{
display:flex;
flex-wrap:wrap;
gap:16px;
margin:10px 0 18px 0;
width:100%;
}

.violencia-col{
flex:1 1 280px;
background-color:#2e3441;
border-radius:12px;
border:1px solid #272B36;
padding:14px 16px;
box-sizing:border-box;
transition:background-color 0.15s ease,border-color 0.15s ease,transform 0.15s ease;
}

.violencia-col:hover{
background-color:#151B2B;
border-color:#3B4253;
transform:translateY(-1px);
}

.violencia-title{
font-size:0.84rem;
text-transform:uppercase;
letter-spacing:0.09em;
color:#9CA3AF;
margin:0 0 6px 0;
}

.violencia-text{
margin:0;
font-size:0.92rem;
line-height:1.6;
color:#E5E7EB;
text-align:justify;
}

@media (max-width:700px){
.violencia-wrapper{
flex-direction:column;
}
}
</style>

<div class="violencia-wrapper">
<div class="violencia-col">
<p class="violencia-title">Panorama general</p>
<p class="violencia-text">
Como se puede evidenciar en el anterior gráfico, la violencia contra la mujer es un problema persistente y generalizado que afecta a mujeres de todas las edades, orígenes y condiciones sociales en Colombia.
</p>
</div>

<div class="violencia-col">
<p class="violencia-title">Implicaciones y necesidad de análisis</p>
<p class="violencia-text">
Este fenómeno incluye diversas formas de abuso, como la violencia física, sexual, psicológica y económica, y tiene profundas repercusiones en la salud, el bienestar y los derechos humanos de las mujeres. Es por ello que es necesario ahondar en las tendencias de esta problemática para diseñar estrategias efectivas de prevención y apoyo a las víctimas.
</p>
</div>
</div>
"""
############################# DELITOS CONTRA LA MUJER #############################
componente_feminicidios = """
<style>

.fem-card {
    background: rgba(255, 255, 255, 0.04);
    border: 1px solid rgba(255, 255, 255, 0.08);
    padding: 30px;
    border-radius: 18px;
    color: #e6e6e6;
    font-family: 'Segoe UI', sans-serif;
    backdrop-filter: blur(4px);
    animation: fadeSlide 1.2s ease forwards;
    opacity: 0;
    transform: translateY(20px);
    transition: transform 0.4s ease, box-shadow 0.4s ease;
}

.fem-card:hover {
    transform: translateY(5px);
    box-shadow: 0px 8px 22px rgba(0, 0, 0, 0.3);
}

.fem-title {
    font-size: 2rem;
    font-weight: 700;
    margin-bottom: 10px;
    color: #f5f5f5;
    letter-spacing: 0.5px;
    text-shadow: 0px 0px 8px rgba(255,255,255,0.08);
}

.fem-line {
    width: 90%;
    height: 3px;
    background: linear-gradient(90deg, #ff4d6d, #ff99ac);
    border-radius: 20px;
    margin: 8px 0 22px 0;
    animation: expandLine 1.4s ease-out forwards;
    transform-origin: left;
    opacity: 0;
}

.fem-text {
    font-size: 1.05rem;
    line-height: 1.6;
    color: #d1d1d1;
    text-align: justify;
}

@keyframes fadeSlide {
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@keyframes expandLine {
    0% { transform: scaleX(0); opacity: 0; }
    100% { transform: scaleX(1); opacity: 1; }
}

</style>

<div class="fem-card">
    <div class="fem-title">Victimas Femeninas por Departamento</div>
    <div class="fem-line"></div>
    <div class="fem-text">
        Como vimos anteriormente, el genero femenino representa una mayoría significativa de las víctimas de delitos sexuales en Colombia.
        Este hecho resalta la urgente necesidad de enfocar esfuerzos en la protección y apoyo a las mujeres afectadas por estas conductas delictivas.
        <br><br>
        Al analizar la distribución por departamento, podemos identificar las regiones donde las mujeres enfrentan mayores riesgos,
        De esta manera, resulta facil observar la distribución geográfica de los casos y detectar patrones que nos ayuden a entener el fenomeno
</div>
"""

componente_tendencia_fem = """
<style>

.fem-trend-card {
background: rgba(255, 255, 255, 0.035);
border: 1px solid rgba(255, 255, 255, 0.07);
padding: 28px;
border-radius: 16px;
color: #e6e6e6;
font-family: 'Segoe UI', sans-serif;
backdrop-filter: blur(3px);
animation: fadeUp 1.1s ease forwards;
opacity: 0;
transform: translateY(24px);
transition: transform 0.4s ease, box-shadow 0.4s ease;
}

.fem-trend-card:hover {
transform: translateY(6px);
box-shadow: 0px 6px 20px rgba(0, 0, 0, 0.28);
}

.fem-trend-title {
font-size: 1.55rem;
font-weight: 700;
margin-bottom: 12px;
color: #f4f4f4;
letter-spacing: 0.3px;
}

.fem-trend-line {
width: 35%;
height: 3px;
background: linear-gradient(90deg, #ff4d6d, #ff99ac);
border-radius: 20px;
margin: 8px 0 20px 0;
animation: growLine 1.3s ease-out forwards;
transform-origin: left;
opacity: 0;
}

.fem-trend-text {
font-size: 1.03rem;
line-height: 1.6;
color: #d1d1d1;
text-align: justify;
}

@keyframes fadeUp {
to {
opacity: 1;
transform: translateY(0);
}
}

@keyframes growLine {
0% { transform: scaleX(0); opacity: 0; }
100% { transform: scaleX(1); opacity: 1; }
}

</style>

<div class="fem-trend-card">
<div class="fem-trend-title">¿Por qué analizar la tendencia anual?</div>
<div class="fem-trend-line"></div>
<div class="fem-trend-text">
  Tras analizar lo anterior, rapidamente nos damos cuenta que los departamentos con mayor número de víctimas femeninas también muestran un aumento constante en los casos reportados año tras año.
  Esta correlación sugiere que ciertos factores regionales podrían estar contribuyendo a la persistencia y el incremento de estos delitos.
  por ejemplo, factores socioeconómicos, culturales, demograficos o incluso la eficacia de las políticas públicas implementadas en cada región.
  <br><br>
  También es importante resaltar que este es el tipo de victima más vulnerable, por ende, es necesario ver como ha evolucionado la situación a lo largo del tiempo para entender mejor el fenómeno y diseñar estrategias efectivas de prevención y apoyo.
  En el siguiente gráfico se observa la tendencia anual de víctimas femeninas por departamento.
</div>
</div>
"""

metric_info_gen = """
<div class="metric-info-container">
<div class="metric-info-box">
NOTA: Los datos solo van hasta Mayo del 2025, por eso la tendencia anual puede no reflejar el comportamiento completo del año.
</div>
"""

