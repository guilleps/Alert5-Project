import axios from "axios";
import { FeedbackPayload, IncidentPredictionInput, PredictionResult } from "./dto";

const API_URL = import.meta.env.VITE_API_URL || "http://localhost:8000";

export async function getPredictions(input: IncidentPredictionInput): Promise<PredictionResult[]> {
  const response = await axios.post<{ top_5: PredictionResult[] }>(`${API_URL}/predict`, input);
  return response.data.top_5;
}

export async function sendFeedback(feedbackPayload: FeedbackPayload): Promise<void> {
  try {
    const response = await axios.post(`${API_URL}/feedback`, feedbackPayload);
    console.log('Feedback enviado con éxito:', response.data);
  } catch (error) {
    console.error('Error al enviar feedback:', error);
    throw new Error('No se pudo enviar la retroalimentación.');
  }
}