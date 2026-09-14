import { useState } from 'react';
import { Folder, Upload, CheckCircle, X, Eye, Trash, Share2, Copy, Download, File, BarChart2, FileText } from 'lucide-react';

const Files = () => {
  const [files, setFiles] = useState([
    {
      id: 1,
      name: 'documento_trabalho.pdf',
      type: 'application/pdf',
      size: '2.4 MB',
      date: '2026-09-10 14:30',
      thumbnail: '/assets/document-preview.png'
    },
    {
      id: 2,
      name: 'foto_familia.jpg',
      type: 'image/jpeg',
      size: '3.2 MB',
      date: '2026-09-09 09:15',
      thumbnail: '/assets/photo-preview.jpg'
    },
    {
      id: 3,
      name: 'planilha_orcamento.xlsx',
      type: 'application/vnd.ms-excel',
      size: '1.8 MB',
      date: '2026-09-08 16:45',
      thumbnail: '/assets/spreadsheet-preview.png'
    }
  ]);
  
  const [selectedFile, setSelectedFile] = useState(null);
  const [uploadProgress, setUploadProgress] = useState(0);
  const [isUploading, setIsUploading] = useState(false);

  const handleFileSelect = (e) => {
    const file = e.target.files[0];
    if (file) {
      // Simulate file processing
      const newFile = {
        id: Date.now(),
        name: file.name,
        type: file.type,
        size: `${(file.size / (1024 * 1024)).toFixed(1)} MB`,
        date: new Date().toISOString().slice(0, 19).replace('T', ' '),
        thumbnail: getFileThumbnail(file.type)
      };
      
      setFiles([newFile, ...files]);
      e.target.value = ''; // Reset input
    }
  };

  const getFileThumbnail = (type) => {
    if (type.startsWith('image/')) return '/assets/image-placeholder.png';
    if (type === 'application/pdf') return '/assets/pdf-placeholder.png';
    if (type.includes('spreadsheet') || type.includes('excel')) return '/assets/excel-placeholder.png';
    if (type.includes('document') || type.includes('word')) return '/assets/doc-placeholder.png';
    return '/assets/file-placeholder.png';
  };

  const handleDelete = (id) => {
    setFiles(files.filter(f => f.id !== id));
  };

  const handleDownload = (file) => {
    // In real app, would trigger actual download
    alert(`Downloading ${file.name}...`);
  };

  return (
    <div className="min-h-screen bg-[#0f0f12]">
      <div className="px-6 py-8">
        <div className="mb-6">
          <h1 className="text-2xl font-bold text-white">
            Arquivos
          </h1>
          <p className="mt-2 text-gray-400">
            Gerencie seus arquivos pessoais com segurança
          </p>
        </div>
        
        {/* Upload Section */}
        <div className="bg-[#1a1a23] rounded-xl p-6 mb-8">
          <div className="flex items-center mb-4">
            <Folder className="h-5 w-5 text-[#8b5cf6] mr-3" />
            <h2 className="text-lg font-semibold text-white">Adicionar arquivos</h2>
          </div>
          
          <div className="border-2 border-dashed border-gray-700 rounded-xl p-8 text-center cursor-pointer hover:border-gray-600 transition-colors" onClick={() => document.getElementById('file-input').click()}>
            <div className="space-y-3">
              <Upload className="h-8 w-8 text-[#8b5cf6] mb-2" />
              <p className="text-gray-300">Clique para selecionar ou arraste arquivos aqui</p>
              <p className="text-xs text-gray-500">
                Formats suportados: PDF, JPG, PNG, DOC, XLSX e mais
              </p>
            </div>
          </div>
          
          <input
            type="file"
            id="file-input"
            className="hidden"
            multiple
            onChange={handleFileSelect}
          />
          
          {isUploading && (
            <div className="mt-4">
              <div className="w-full bg-gray-800 rounded-full h-2.5 mb-2">
                <div 
                  className="bg-gradient-to-r from-[#8b5cf6] to-[#06b6d4] h-2.5 rounded-full" 
                  style={{ width: `${uploadProgress}%` }}
                ></div>
              </div>
              <p className="text-right text-sm text-gray-400">
                {uploadProgress}% completo
              </p>
            </div>
          )}
        </div>
        
        {/* Files List */}
        <div className="space-y-4">
          {files.length === 0 ? (
            <div className="text-center py-12">
              <Folder className="h-12 w-12 mx-auto mb-4 text-gray-600" />
              <p className="text-gray-500">Nenhum arquivo ainda</p>
              <p className="text-sm text-gray-400 mt-2">
                Adicione seus primeiros arquivos para começar
              </p>
            </div>
          ) : (
            <div className="space-y-4">
              {files.map((file) => (
                <div key={file.id} className="bg-[#1a1a23] rounded-xl p-4 flex items-center justify-between">
                  <div className="flex items-center space-x-4">
                    <div className="flex-shrink-0">
                      <div className="bg-[#8b5cf6]/20 rounded-lg p-3 flex items-center justify-center w-10 h-10">
                        {getFileIcon(file.type)}
                      </div>
                    </div>
                    <div className="flex-1 min-w-0">
                      <div className="flex justify-between">
                        <h3 className="font-semibold text-white truncate max-w-[200px]">
                          {file.name}
                        </h3>
                        <span className="text-xs text-gray-500">{file.size}</span>
                      </div>
                      <p className="text-gray-400 mt-1 text-sm">
                        {file.date.split(' ')[0]} às {file.date.split(' ')[1]}
                      </p>
                    </div>
                    <div className="flex items-center space-x-3 text-sm">
                      <button onClick={() => handleDownload(file)} title="Download" className="hover:text-gray-300 transition-colors">
                        <Download className="h-4 w-4" />
                      </button>
                      <button onClick={() => setSelectedFile(file)} title="Visualizar" className="hover:text-gray-300 transition-colors">
                        <Eye className="h-4 w-4" />
                      </button>
                      <button onClick={() => handleCopyLink(file)} title="Copiar link" className="hover:text-gray-300 transition-colors">
                        <Copy className="h-4 w-4" />
                      </button>
                      <button onClick={() => handleDelete(file.id)} title="Excluir" className="hover:text-red-400 transition-colors text-red-400">
                        <Trash className="h-4 w-4" />
                      </button>
                    </div>
                  </div>
                </div>
              ))}
            </div>
          )}
        </div>
        
        {/* File Preview Modal */}
        {selectedFile && (
          <div className="fixed inset-0 bg-black/50 flex items-center justify-center z-50 p-4">
            <div className="bg-[#1a1a23] rounded-xl p-6 max-w-2xl w-full max-h-[90vh] overflow-y-auto">
              <div className="flex justify-between items-start mb-4">
                <h2 className="text-xl font-semibold text-white">
                  {selectedFile.name}
                </h2>
                <button onClick={() => setSelectedFile(null)} className="text-gray-400 hover:text-white">
                  <X className="h-5 w-5" />
                </button>
              </div>
              
              <div className="space-y-6">
                <div className="text-center">
                  <div className="bg-gray-800 rounded-xl p-8">
                    {getFilePreview(selectedFile.type)}
                  </div>
                  <p className="mt-4 text-gray-400 text-sm">
                    {selectedFile.type} • {selectedFile.size}
                  </p>
                </div>
                
                <div className="flex items-center justify-between">
                  <div className="flex items-center space-x-3">
                    <span className="text-gray-500">Modificado:</span>
                    <span className="text-white">{selectedFile.date}</span>
                  </div>
                  <div className="flex items-center space-x-4">
                    <button onClick={() => handleDownload(selectedFile)} className="btn-outline">
                      <Download className="h-4 w-4" /> Download
                    </button>
                    <button onClick={() => handleShareFile(selectedFile)} className="btn-outline">
                      <Share2 className="h-4 w-4" /> Compartilhar
                    </button>
                  </div>
                </div>
              </div>
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

// Helper functions for file icons and previews
const getFileIcon = (type) => {
  if (type.startsWith('image/')) return <img src="/assets/image-icon.png" alt="image" className="h-4 w-4" />;
  if (type === 'application/pdf') return <File className="h-4 w-4" />;
  if (type.includes('spreadsheet') || type.includes('excel')) return <BarChart2 className="h-4 w-4" />;
  if (type.includes('document') || type.includes('word')) return <FileText className="h-4 w-4" />;
  return <File className="h-4 w-4" />;
};

const getFilePreview = (type) => {
  if (type.startsWith('image/')) {
    return <img src="/assets/image-preview-large.png" alt="preview" className="rounded-lg w-full h-96 object-cover" />;
  }
  if (type === 'application/pdf') {
    return (
      <div className="flex items-center justify-center h-96 bg-gray-800 rounded-lg">
        <div className="text-center">
          <File className="h-10 w-10 text-gray-400 mb-3" />
          <p className="text-gray-400">Documento PDF</p>
        </div>
      </div>
    );
  }
  // Default preview
  return (
    <div className="flex items-center justify-center h-96 bg-gray-800 rounded-lg">
      <div className="text-center">
        <File className="h-8 w-8 text-gray-400 mb-3" />
        <p className="text-gray-400">Visualização não disponível</p>
      </div>
    </div>
  );
};

const handleCopyLink = (file) => {
  // In real app, would copy shareable link to clipboard
  alert(`Link copiado: https://flowai.cloud/files/${file.id}`);
};

const handleShareFile = (file) => {
  // In real app, would open share dialog
  alert(`Compartilhando ${file.name}...`);
};

export default Files;
