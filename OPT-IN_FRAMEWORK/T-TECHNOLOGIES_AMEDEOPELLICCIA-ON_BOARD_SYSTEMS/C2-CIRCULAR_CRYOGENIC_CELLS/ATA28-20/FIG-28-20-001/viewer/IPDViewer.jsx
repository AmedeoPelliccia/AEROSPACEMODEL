/**
 * IPDViewer.jsx
 * ─────────────────────────────────────────────────────────────────────────────
 * AMPEL360 Q100 — ATA 28-20 Cryogenic H₂ Shut-Off Valve
 * Illustrated Parts Data (IPD) Viewer – FIG-28-20-001 REV A
 *
 * Refactored component per OPT-IN_FRAMEWORK canonical architecture (TLI v2.1).
 * All data is imported from sibling JSON files; NO hardcoded data in this module.
 *
 * DMC    : DMC-AMPEL360-A-28-20-00-00A-040A-D
 * SSOT   : SSOT-Q100-C2-004
 * DPP    : DPP-ATA28-20-001
 * BL     : BL-28-004  |  LC04 – Design Definition
 * SC     : SC-28-H2-001, SC-28-CRYO-002
 * ─────────────────────────────────────────────────────────────────────────────
 */

import React, { useState, useMemo } from 'react';

// ── External data imports (OPT-IN_FRAMEWORK canonical data artifacts) ────────
import partsData       from '../parts_list.json';
import crossRefsData   from '../cross_references.json';
import sourceData      from '../source_data.json';
import figureMetadata  from '../figure_metadata.json';

// ── Extract arrays from data files ──────────────────────────────────────────
const PARTS_DATA  = partsData.parts;
const CROSS_REFS  = crossRefsData.cross_references;
const SOURCE_DATA = sourceData.sources;
const HOTSPOT_POSITIONS = figureMetadata.hotspot_map;

// ── Category display configuration ──────────────────────────────────────────
const CAT_COLORS = {
  assy:        { bg: 'bg-blue-100',   text: 'text-blue-800',   border: 'border-blue-200'   },
  detail:      { bg: 'bg-gray-100',   text: 'text-gray-800',   border: 'border-gray-200'   },
  consumable:  { bg: 'bg-amber-100',  text: 'text-amber-800',  border: 'border-amber-200'  },
  standard:    { bg: 'bg-green-100',  text: 'text-green-800',  border: 'border-green-200'  },
};

const CAT_LABELS = {
  assy:       'Assembly',
  detail:     'Detail Part',
  consumable: 'Consumable',
  standard:   'Standard Part',
};

// ── Cross-reference type badge colours ───────────────────────────────────────
const XREF_COLORS = {
  AMM:  { bg: 'bg-blue-50',   text: 'text-blue-700',   border: 'border-blue-300'  },
  CMM:  { bg: 'bg-purple-50', text: 'text-purple-700', border: 'border-purple-300'},
  TSM:  { bg: 'bg-red-50',    text: 'text-red-700',    border: 'border-red-300'   },
  SB:   { bg: 'bg-orange-50', text: 'text-orange-700', border: 'border-orange-300'},
  SRM:  { bg: 'bg-teal-50',   text: 'text-teal-700',   border: 'border-teal-300'  },
  WDM:  { bg: 'bg-indigo-50', text: 'text-indigo-700', border: 'border-indigo-300'},
  KNOT: { bg: 'bg-pink-50',   text: 'text-pink-700',   border: 'border-pink-300'  },
};

// ── Source status badge colours ───────────────────────────────────────────────
const STATUS_COLORS = {
  'APPROVED':  { bg: 'bg-green-100',  text: 'text-green-800'  },
  'QUAL-TEST': { bg: 'bg-yellow-100', text: 'text-yellow-800' },
  'DRAFT':     { bg: 'bg-gray-100',   text: 'text-gray-700'   },
  'REJECTED':  { bg: 'bg-red-100',    text: 'text-red-800'    },
};

// ── Tabs definition ───────────────────────────────────────────────────────────
const TABS = [
  { id: 'drawing',    label: 'Drawing',         icon: '⬡' },
  { id: 'parts',      label: 'Parts List',      icon: '≡' },
  { id: 'crossref',   label: 'Cross-References', icon: '↗' },
  { id: 'sources',    label: 'Source Data',      icon: '◎' },
];

// ═════════════════════════════════════════════════════════════════════════════
// TechnicalDrawing – inline SVG viewer with hotspot interaction
// ═════════════════════════════════════════════════════════════════════════════
function TechnicalDrawing({ onHotspotClick, activeHotspot }) {
  const { figure_id, revision, issue_date, title, dmc, sheet, scale } = figureMetadata;

  return (
    <div className="relative w-full border border-gray-200 rounded-lg overflow-hidden bg-white shadow-sm">
      {/* Drawing title bar */}
      <div className="bg-slate-800 text-white px-4 py-2 flex items-center justify-between text-xs font-mono">
        <span className="text-slate-300">{dmc}</span>
        <span className="font-bold tracking-widest">{figure_id} REV {revision}</span>
        <span className="text-slate-300">{scale} · {sheet} · {issue_date}</span>
      </div>

      {/* SVG drawing with hotspot overlays */}
      <div className="relative" style={{ paddingBottom: '75%' }}>
        <div className="absolute inset-0 flex items-center justify-center p-4">
          {/* Embed the static drawing.svg */}
          <object
            data="../drawing.svg"
            type="image/svg+xml"
            className="w-full h-full object-contain"
            aria-label={title}
          >
            <img src="../drawing.svg" alt={title} className="w-full h-full object-contain"/>
          </object>

          {/* Interactive hotspot overlays positioned from figure_metadata.json */}
          {Object.entries(HOTSPOT_POSITIONS).map(([letter, pos]) => {
            const isActive = activeHotspot === letter;
            return (
              <button
                key={letter}
                onClick={() => onHotspotClick(letter)}
                title={`Item ${pos.item} – Hotspot ${letter}`}
                aria-label={`Hotspot ${letter}, item ${pos.item}`}
                className={`absolute flex items-center justify-center rounded-full text-xs font-bold font-mono transition-all
                  ${isActive
                    ? 'w-7 h-7 bg-orange-500 text-white border-2 border-orange-700 shadow-lg scale-125 z-20'
                    : 'w-6 h-6 bg-blue-600 text-white border border-blue-800 shadow hover:bg-blue-500 hover:scale-110 z-10'
                  }`}
                style={{
                  left:   `${pos.x_pct}%`,
                  top:    `${pos.y_pct}%`,
                  transform: 'translate(-50%, -50%)',
                }}
              >
                {letter}
              </button>
            );
          })}
        </div>
      </div>

      {/* Drawing footer */}
      <div className="bg-slate-100 border-t border-gray-200 px-4 py-1 flex items-center gap-6 text-xs text-slate-500 font-mono">
        <span>ATA {figureMetadata.ata_chapter}</span>
        <span>DRAWN: {figureMetadata.drawn_by}</span>
        <span>CHKD: {figureMetadata.checked_by}</span>
        <span className="ml-auto text-amber-600 font-semibold">⭐ Novel Technology — SC-28-H2-001</span>
      </div>
    </div>
  );
}

// ═════════════════════════════════════════════════════════════════════════════
// PartDetailPanel – slide-in panel showing selected part details
// ═════════════════════════════════════════════════════════════════════════════
function PartDetailPanel({ part, onClose }) {
  if (!part) return null;
  const cat = CAT_COLORS[part.category] || CAT_COLORS.detail;

  return (
    <div className="fixed right-0 top-0 h-full w-80 bg-white shadow-2xl border-l border-gray-200 z-50 overflow-y-auto">
      <div className="bg-slate-800 text-white px-4 py-3 flex items-center justify-between sticky top-0">
        <span className="font-mono font-bold text-sm">
          Item {part.item} — Hotspot {part.hotspot}
        </span>
        <button
          onClick={onClose}
          className="text-slate-400 hover:text-white text-xl leading-none"
          aria-label="Close detail panel"
        >
          ×
        </button>
      </div>

      <div className="p-4 space-y-4">
        {/* Part number and nomenclature */}
        <div>
          <p className="text-xs text-gray-500 font-mono uppercase tracking-wide">Part Number</p>
          <p className="font-mono font-bold text-blue-700 text-sm">{part.pn}</p>
        </div>
        <div>
          <p className="text-xs text-gray-500 font-mono uppercase tracking-wide">Nomenclature</p>
          <p className="font-semibold text-gray-900 text-sm leading-snug">{part.nomenclature}</p>
        </div>

        {/* Category badge */}
        <div>
          <span className={`inline-block px-2 py-0.5 rounded text-xs font-semibold border ${cat.bg} ${cat.text} ${cat.border}`}>
            {CAT_LABELS[part.category] || part.category}
          </span>
        </div>

        {/* Grid of key fields */}
        <div className="grid grid-cols-2 gap-3 text-xs">
          {[
            ['Qty / Unit', `${part.qty} ${part.unit}`],
            ['SMR Code',   part.smr],
            ['CSN',        part.csn],
            ['ATA',        part.ata],
            ['Effectivity', part.effectivity],
            ['CAGE',       part.cage],
          ].map(([label, value]) => value && (
            <div key={label}>
              <p className="text-gray-500 font-mono uppercase tracking-wide text-xs">{label}</p>
              <p className="font-mono text-gray-800">{value}</p>
            </div>
          ))}
        </div>

        {/* Source */}
        {part.source && (
          <div>
            <p className="text-xs text-gray-500 font-mono uppercase tracking-wide">Approved Source</p>
            <p className="font-mono text-sm text-green-700">{part.source}</p>
          </div>
        )}

        {/* IPC reference */}
        {part.ipc_ref && (
          <div>
            <p className="text-xs text-gray-500 font-mono uppercase tracking-wide">IPC/CMM Ref</p>
            <p className="text-sm text-gray-700 italic">{part.ipc_ref}</p>
          </div>
        )}

        {/* Note */}
        {part.note && (
          <div className="bg-amber-50 border border-amber-200 rounded p-2">
            <p className="text-xs text-amber-700 font-mono uppercase tracking-wide mb-1">Note</p>
            <p className="text-xs text-amber-900 leading-relaxed">{part.note}</p>
          </div>
        )}
      </div>
    </div>
  );
}

// ═════════════════════════════════════════════════════════════════════════════
// IPDViewer – main component
// ═════════════════════════════════════════════════════════════════════════════
export default function IPDViewer() {
  const [activeTab,     setActiveTab]     = useState('drawing');
  const [activeHotspot, setActiveHotspot] = useState(null);
  const [selectedPart,  setSelectedPart]  = useState(null);
  const [searchQuery,   setSearchQuery]   = useState('');
  const [categoryFilter, setCategoryFilter] = useState('all');

  // ── Hotspot click handler ─────────────────────────────────────────────────
  const handleHotspotClick = (letter) => {
    const hotspotPos = HOTSPOT_POSITIONS[letter];
    if (!hotspotPos) return;
    const part = PARTS_DATA.find(p => p.item === hotspotPos.item);
    setActiveHotspot(letter);
    setSelectedPart(part || null);
    if (part) setActiveTab('parts');
  };

  // ── Filtered parts list ───────────────────────────────────────────────────
  const filteredParts = useMemo(() => {
    const q = searchQuery.toLowerCase();
    return PARTS_DATA.filter(part => {
      const matchesCat = categoryFilter === 'all' || part.category === categoryFilter;
      const matchesQuery = !q
        || part.pn.toLowerCase().includes(q)
        || part.nomenclature.toLowerCase().includes(q)
        || String(part.item).includes(q)
        || (part.hotspot && part.hotspot.toLowerCase().includes(q))
        || (part.csn && part.csn.toLowerCase().includes(q));
      return matchesCat && matchesQuery;
    });
  }, [searchQuery, categoryFilter]);

  return (
    <div className="min-h-screen bg-slate-50 font-sans">
      {/* ── Header ─────────────────────────────────────────────────────────── */}
      <header className="bg-slate-900 text-white shadow-lg">
        <div className="max-w-7xl mx-auto px-4 py-4">
          <div className="flex items-start justify-between">
            <div>
              <p className="text-xs text-slate-400 font-mono tracking-widest uppercase mb-1">
                AMPEL360 Q100 · ATA {figureMetadata.ata_chapter} · IPD Viewer
              </p>
              <h1 className="text-xl font-bold text-white leading-tight">
                {figureMetadata.title}
              </h1>
              <p className="text-sm text-slate-300 font-mono mt-1">
                {figureMetadata.figure_id} REV {figureMetadata.revision}
                &nbsp;·&nbsp;
                {figureMetadata.dmc}
              </p>
            </div>
            <div className="text-right hidden md:block">
              <span className="inline-block bg-amber-500 text-white text-xs font-bold px-2 py-1 rounded">
                ⭐ Novel Technology
              </span>
              <p className="text-xs text-slate-400 mt-1 font-mono">SC-28-H2-001 · SC-28-CRYO-002</p>
            </div>
          </div>
        </div>
      </header>

      {/* ── Safety Banner ──────────────────────────────────────────────────── */}
      <div className="bg-red-700 text-white">
        <div className="max-w-7xl mx-auto px-4 py-2 flex items-center gap-3 text-sm">
          <span className="text-lg">⚠️</span>
          <span className="font-bold">DANGER —</span>
          <span>LH₂ at –253°C. Cryogenic burn hazard. H₂ is extremely flammable (4–75% in air). Full PPE required. No ignition sources within 15 m.</span>
        </div>
      </div>

      {/* ── Main content ───────────────────────────────────────────────────── */}
      <main className="max-w-7xl mx-auto px-4 py-6">

        {/* Tab navigation */}
        <nav className="flex space-x-1 border-b border-gray-200 mb-6" role="tablist">
          {TABS.map(tab => (
            <button
              key={tab.id}
              role="tab"
              aria-selected={activeTab === tab.id}
              onClick={() => setActiveTab(tab.id)}
              className={`px-4 py-2 text-sm font-medium rounded-t border-b-2 transition-colors
                ${activeTab === tab.id
                  ? 'border-blue-600 text-blue-700 bg-white'
                  : 'border-transparent text-gray-600 hover:text-gray-900 hover:bg-gray-50'
                }`}
            >
              <span className="mr-1.5">{tab.icon}</span>
              {tab.label}
              {tab.id === 'parts'    && <span className="ml-1.5 text-xs bg-blue-100 text-blue-700 px-1.5 py-0.5 rounded-full">{PARTS_DATA.length}</span>}
              {tab.id === 'crossref' && <span className="ml-1.5 text-xs bg-gray-100 text-gray-700 px-1.5 py-0.5 rounded-full">{CROSS_REFS.length}</span>}
              {tab.id === 'sources'  && <span className="ml-1.5 text-xs bg-gray-100 text-gray-700 px-1.5 py-0.5 rounded-full">{SOURCE_DATA.length}</span>}
            </button>
          ))}
        </nav>

        {/* ── Tab: Drawing ─────────────────────────────────────────────────── */}
        {activeTab === 'drawing' && (
          <div>
            <TechnicalDrawing
              onHotspotClick={handleHotspotClick}
              activeHotspot={activeHotspot}
            />
            {activeHotspot && (
              <p className="mt-3 text-sm text-center text-gray-500 font-mono">
                Selected hotspot: <strong className="text-blue-700">{activeHotspot}</strong>
                {' — '}
                <button
                  onClick={() => setActiveTab('parts')}
                  className="text-blue-600 underline hover:text-blue-800"
                >
                  View in Parts List
                </button>
              </p>
            )}
          </div>
        )}

        {/* ── Tab: Parts List ──────────────────────────────────────────────── */}
        {activeTab === 'parts' && (
          <div>
            {/* Search and filter controls */}
            <div className="flex flex-col sm:flex-row gap-3 mb-4">
              <input
                type="search"
                placeholder="Search by PN, nomenclature, item, CSN…"
                value={searchQuery}
                onChange={e => setSearchQuery(e.target.value)}
                className="flex-1 border border-gray-300 rounded-lg px-3 py-2 text-sm shadow-sm
                           focus:outline-none focus:ring-2 focus:ring-blue-500 font-mono"
                aria-label="Search parts"
              />
              <select
                value={categoryFilter}
                onChange={e => setCategoryFilter(e.target.value)}
                className="border border-gray-300 rounded-lg px-3 py-2 text-sm shadow-sm
                           focus:outline-none focus:ring-2 focus:ring-blue-500"
                aria-label="Filter by category"
              >
                <option value="all">All Categories</option>
                {Object.entries(CAT_LABELS).map(([key, label]) => (
                  <option key={key} value={key}>{label}</option>
                ))}
              </select>
            </div>

            {/* Parts table */}
            <div className="overflow-x-auto rounded-lg border border-gray-200 shadow-sm">
              <table className="w-full text-xs font-mono border-collapse">
                <thead>
                  <tr className="bg-slate-800 text-white">
                    {['Hs', 'Item', 'Part Number', 'Nomenclature', 'Qty', 'Unit', 'SMR', 'Category', 'Source', 'ATA'].map(h => (
                      <th key={h} className="px-3 py-2 text-left font-semibold tracking-wide uppercase">{h}</th>
                    ))}
                  </tr>
                </thead>
                <tbody>
                  {filteredParts.map((part, idx) => {
                    const cat = CAT_COLORS[part.category] || CAT_COLORS.detail;
                    const isSelected = selectedPart?.item === part.item;
                    return (
                      <tr
                        key={part.item}
                        onClick={() => setSelectedPart(isSelected ? null : part)}
                        className={`border-b border-gray-100 cursor-pointer transition-colors
                          ${isSelected
                            ? 'bg-blue-50 ring-1 ring-inset ring-blue-300'
                            : idx % 2 === 0 ? 'bg-white hover:bg-blue-50' : 'bg-slate-50 hover:bg-blue-50'
                          }`}
                      >
                        <td className="px-3 py-1.5">
                          {part.hotspot && (
                            <button
                              onClick={e => { e.stopPropagation(); handleHotspotClick(part.hotspot); setActiveTab('drawing'); }}
                              className={`w-6 h-6 rounded-full text-xs font-bold flex items-center justify-center
                                ${activeHotspot === part.hotspot
                                  ? 'bg-orange-500 text-white'
                                  : 'bg-blue-600 text-white hover:bg-blue-500'
                                }`}
                              title={`Go to hotspot ${part.hotspot} on drawing`}
                            >
                              {part.hotspot}
                            </button>
                          )}
                        </td>
                        <td className="px-3 py-1.5 font-bold text-gray-700">{part.item}</td>
                        <td className="px-3 py-1.5 text-blue-700 font-bold">{part.pn}</td>
                        <td className="px-3 py-1.5 text-gray-900 max-w-xs truncate" title={part.nomenclature}>{part.nomenclature}</td>
                        <td className="px-3 py-1.5 text-center">{part.qty}</td>
                        <td className="px-3 py-1.5 text-center">{part.unit}</td>
                        <td className="px-3 py-1.5 text-gray-600">{part.smr}</td>
                        <td className="px-3 py-1.5">
                          <span className={`px-1.5 py-0.5 rounded text-xs font-semibold ${cat.bg} ${cat.text}`}>
                            {CAT_LABELS[part.category] || part.category}
                          </span>
                        </td>
                        <td className="px-3 py-1.5 text-green-700">{part.source}</td>
                        <td className="px-3 py-1.5 text-gray-500">{part.ata}</td>
                      </tr>
                    );
                  })}
                  {filteredParts.length === 0 && (
                    <tr>
                      <td colSpan={10} className="px-4 py-8 text-center text-gray-400 italic">
                        No parts match the current filter.
                      </td>
                    </tr>
                  )}
                </tbody>
              </table>
            </div>
            <p className="mt-2 text-xs text-gray-400 font-mono text-right">
              Showing {filteredParts.length} of {PARTS_DATA.length} items · Click a row for details
            </p>
          </div>
        )}

        {/* ── Tab: Cross-References ─────────────────────────────────────────── */}
        {activeTab === 'crossref' && (
          <div className="space-y-3">
            {CROSS_REFS.map((xref, idx) => {
              const colors = XREF_COLORS[xref.type] || XREF_COLORS.AMM;
              return (
                <div
                  key={idx}
                  className={`flex items-start gap-4 p-4 rounded-lg border ${colors.bg} ${colors.border}`}
                >
                  <span className={`shrink-0 px-2 py-1 rounded text-xs font-bold font-mono ${colors.text} ${colors.bg} border ${colors.border}`}>
                    {xref.type}
                  </span>
                  <div className="flex-1 min-w-0">
                    <p className={`font-semibold text-sm ${colors.text} truncate`} title={xref.title}>
                      {xref.title}
                    </p>
                    <p className="text-xs font-mono text-gray-500 mt-0.5 truncate" title={xref.ref}>
                      {xref.ref}
                    </p>
                    {xref.ata && (
                      <p className="text-xs text-gray-400 mt-0.5">ATA {xref.ata}</p>
                    )}
                  </div>
                </div>
              );
            })}
          </div>
        )}

        {/* ── Tab: Source Data ──────────────────────────────────────────────── */}
        {activeTab === 'sources' && (
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
            {SOURCE_DATA.map(src => {
              const sc = STATUS_COLORS[src.status] || STATUS_COLORS.DRAFT;
              return (
                <div key={src.id} className="bg-white border border-gray-200 rounded-lg shadow-sm p-4 space-y-2">
                  <div className="flex items-center justify-between">
                    <span className="text-xs font-mono font-bold text-blue-700">{src.id}</span>
                    <span className={`text-xs font-bold px-2 py-0.5 rounded ${sc.bg} ${sc.text}`}>
                      {src.status}
                    </span>
                  </div>
                  <p className="text-sm font-semibold text-gray-900 leading-snug">{src.title}</p>
                  <p className="text-xs text-gray-600">{src.vendor}</p>
                  <p className="text-xs text-gray-400 font-mono">{src.date}</p>
                </div>
              );
            })}
          </div>
        )}
      </main>

      {/* ── Part Detail Side Panel ─────────────────────────────────────────── */}
      {selectedPart && activeTab === 'parts' && (
        <PartDetailPanel
          part={selectedPart}
          onClose={() => setSelectedPart(null)}
        />
      )}

      {/* ── Traceability Footer ────────────────────────────────────────────── */}
      <footer className="mt-8 border-t border-gray-200 bg-slate-100">
        <div className="max-w-7xl mx-auto px-4 py-4">
          <div className="flex flex-wrap gap-x-6 gap-y-1 text-xs font-mono text-slate-500">
            <span>SSOT: <strong className="text-slate-700">SSOT-Q100-C2-004</strong></span>
            <span>DPP: <strong className="text-slate-700">DPP-ATA28-20-001</strong></span>
            <span>BL: <strong className="text-slate-700">{figureMetadata.baseline_ref}</strong></span>
            <span>LC: <strong className="text-slate-700">LC04 – Design Definition</strong></span>
            <span>Issued: <strong className="text-slate-700">{figureMetadata.issue_date}</strong></span>
            <span>DMC: <strong className="text-slate-700">{figureMetadata.dmc}</strong></span>
          </div>
          <p className="mt-2 text-xs text-slate-400 font-mono">
            Authority: ASIT · Contract: KITDM-CTR-LM-CSDB_ATA28_H2 · © AMPEL360 Q100 Programme
          </p>
        </div>
      </footer>
    </div>
  );
}
