export interface IncidentPredictionInput {
    año: number;
    mes: number;
    día: number;
    nombre_dia: string;     // 'Lunes', 'Martes', etc.
    turno: 'Mañana' | 'Tarde' | 'Noche';
    sector_nombre: string;
}

export interface PredictionResult {
    grupo_incidente: string;
    probabilidad: number;
}

export interface FeedbackPayload {
    timestamp: string;
    input_data: { fecha: string; turno: string; sector: string };
    predicted: string[];
    feedback: string;
    actual_incident: string[];
}