export interface IncidentPredictionInput {
    año: number;
    mes: number;
    día: number;
    nombre_dia: string;     // 'Lunes', 'Martes', etc.
    turno: 'Mañana' | 'Tarde' | 'Noche';
    sector_nombre: string;
}

export interface PredictionResult {
    grupo: string;
    probabilidad: number;
}
