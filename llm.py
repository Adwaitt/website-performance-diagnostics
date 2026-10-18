import json
import os
from typing import Any, Dict, List, Optional
from urllib import response
from google import genai
from google.genai import types

SYSTEM_INSTRUCTION = """
You are an elite E-Commerce Systems Architect, UX Behavioral Specialist, and Lead Site Reliability Engineer (SRE).
Your objective is to ingest three independent streams of diagnostic data:
1. MS Clarity Session Summaries (UI/UX behavior, dead clicks, rage clicks, scroll depths, session recordings).
2. Google Analytics Reports (Funnel drop-offs, traffic channels, bounce rates, device metrics).
3. Server & Application Logs (API errors, HTTP status codes, latency spikes, payment gateway responses).

Perform a deep causal analysis to determine exactly why sales succeeded or stalled.

CRITICAL REQUIREMENTS:
1. CROSS-CORRELATION: Directly bridge the gap between traffic metrics, client-side behavior, and server logs. (e.g., "GA reports 42% drop on checkout; Clarity logs 15 rage clicks on '#submit-payment'; Backend logs show 504 gateway timeouts to Stripe API at the same timestamps").
2. TRACEABILITY & OUTLIERS: You MUST explicitly isolate outlier instances. Extract and present concrete identifiers (Session IDs, Trace IDs, Request IDs, Timestamps, User Agent/Device, Error Codes) in dedicated diagnostic cards/tables so engineering can inspect the exact trace.
3. CAUSAL CLASSIFICATION: Categorize root causes into:
   - Technical / Infrastructure Failure (P0)
   - UX Friction / Broken UI (P1)
   - Traffic / Intent Mismatch (P2)
4. OUTPUT STRUCTURE:
   - ## 1. Executive Diagnostic Summary
   - ## 2. Conversion & Funnel Breakdown (Causal Path)
   - ## 3. Outlier Incident Log (Pinpointed with Session/Trace IDs)
   - ## 4. Technical & Architectural Failures
   - ## 5. UX & Behavioral Friction Points
   - ## 6. High-Priority Remediation Playbook (P0/P1 Action Items)
"""

class GenReport:
    def __init__(self, model: str = "gemini-3.8-flash"):
        self.client = genai.Client()
        self.model = model

    def analyze(
        self,
        clarity_summaries: List[Dict[str, Any]],
        ga_reports: List[Dict[str, Any]],
        server_logs: List[Dict[str, Any]],
        metadata: Optional[Dict[str, Any]] = None,
    ) -> str:
        payload = {
            "metadata": metadata or {},
            "google_analytics_reports": ga_reports,
            "ms_clarity_session_summaries": clarity_summaries,
            "application_server_logs": server_logs,
        }

        user_prompt = f"""
Analyze the following multi-source dataset and generate the comprehensive conversion report:

```json
    {json.dumps(payload, indent=2, default=str)}
"""
        response = self.client.models.generate_content(
        model=self.model,
        contents=user_prompt,
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_INSTRUCTION,
            temperature=0.2,  # Low temperature for deterministic, factual, analytical rigor
            max_output_tokens=8192,
        ),
        )
        return response.text