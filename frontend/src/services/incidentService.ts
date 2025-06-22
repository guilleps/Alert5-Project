import axios from "axios";
import { IncidentPredictionInput, PredictionResult } from "./dto";

const API_URL = import.meta.env.VITE_API_URL || "http://localhost:8000";

export async function getPredictions(input: IncidentPredictionInput): Promise<PredictionResult[]> {
  const response = await axios.post<{ top_5: PredictionResult[] }>(`${API_URL}/predict`, input);
  return response.data.top_5;
}