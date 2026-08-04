'use client';

import React, { useState } from 'react';

export default function Home() {
  const [selectedFile, setSelectedFile] = useState(null);
  const [mediaType, setMediaType] = useState('image');
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);

  const handleFileChange = (e) => {
    setSelectedFile(e.target.files[0]);
    setResult(null);
  };

  const analyzeMedia = async () => {
    if (!selectedFile) return alert("Please select a file first!");
    setLoading(true);
    setResult(null);

    const formData = new FormData();
    formData.append("file", selectedFile);

    try {
      const res = await fetch(`https://deepshield-backend-0kr6.onrender.com/analyze/`, {
        method: "POST",
        body: formData,
      });
      const data = await res.json();
      setResult(data);
    } catch (error) {
      alert("Error analyzing file. Make sure backend server is running!");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ minHeight: '100vh', backgroundColor: '#020617', color: '#fff', padding: '32px', fontFamily: 'sans-serif' }}>
      <header style={{ textAlign: 'center', marginBottom: '40px' }}>
        <h1 style={{ color: '#22d3ee', fontSize: '28px', fontWeight: 'bold' }}>DEEPSHIELD AI FORENSICS</h1>
      </header>

      <main style={{ maxWidth: '600px', margin: '0 auto', backgroundColor: '#0f172a', padding: '24px', borderRadius: '16px', border: '1px solid #1e293b' }}>
        <div style={{ display: 'flex', justifyContent: 'center', gap: '10px', marginBottom: '20px' }}>
          <button onClick={() => { setMediaType('image'); setResult(null); }} style={{ padding: '8px 16px', borderRadius: '8px', border: 'none', cursor: 'pointer', backgroundColor: mediaType === 'image' ? '#0891b2' : '#334155', color: '#fff' }}>Image ELA</button>
          <button onClick={() => { setMediaType('audio'); setResult(null); }} style={{ padding: '8px 16px', borderRadius: '8px', border: 'none', cursor: 'pointer', backgroundColor: mediaType === 'audio' ? '#0891b2' : '#334155', color: '#fff' }}>Audio Clone</button>
          <button onClick={() => { setMediaType('video'); setResult(null); }} style={{ padding: '8px 16px', borderRadius: '8px', border: 'none', cursor: 'pointer', backgroundColor: mediaType === 'video' ? '#0891b2' : '#334155', color: '#fff' }}>Video Deepfake</button>
        </div>

        <div style={{ border: '2px dashed #334155', padding: '30px', textAlign: 'center', borderRadius: '12px', marginBottom: '20px' }}>
          <input type="file" onChange={handleFileChange} style={{ color: '#94a3b8' }} />
        </div>

        <button onClick={analyzeMedia} disabled={loading} style={{ width: '100%', padding: '12px', borderRadius: '8px', border: 'none', backgroundColor: '#06b6d4', color: '#0f172a', fontWeight: 'bold', cursor: 'pointer' }}>
          {loading ? "Analyzing..." : "Run Forensic Analysis"}
        </button>

        {result && (
          <div style={{ marginTop: '24px', padding: '16px', backgroundColor: '#020617', borderRadius: '8px', border: '1px solid #334155' }}>
            <h3 style={{ color: result.authenticity_score > 70 ? '#4ade80' : '#f87171' }}>
              Status: {result.status}
            </h3>
            <p>Authenticity Score: <strong>{result.authenticity_score}%</strong></p>
            <p style={{ color: '#94a3b8', fontSize: '14px' }}>{result.details}</p>
          </div>
        )}
      </main>
    </div>
  );
}
