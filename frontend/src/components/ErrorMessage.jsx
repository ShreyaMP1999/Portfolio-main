import React from 'react';
import { AlertCircle, RefreshCw } from 'lucide-react';
import { Button } from './ui/button';

const ErrorMessage = ({ 
  message = 'Something went wrong', 
  onRetry, 
  className = '',
  showRetry = true 
}) => {
  return (
    <div className={`flex flex-col items-center justify-center py-12 ${className}`}>
      <div className="flex items-center justify-center w-16 h-16 bg-red-100 rounded-full mb-4">
        <AlertCircle className="w-8 h-8 text-red-600" />
      </div>
      <h3 className="text-lg font-semibold text-gray-900 mb-2">Oops! Something went wrong</h3>
      <p className="text-gray-600 text-center mb-6 max-w-md">{message}</p>
      {showRetry && onRetry && (
        <Button 
          onClick={onRetry}
          className="flex items-center gap-2 bg-blue-600 hover:bg-blue-700"
        >
          <RefreshCw className="w-4 h-4" />
          Try Again
        </Button>
      )}
    </div>
  );
};

export const ErrorCard = ({ message, onRetry, className = '' }) => {
  return (
    <div className={`bg-white rounded-xl shadow-md p-8 ${className}`}>
      <ErrorMessage message={message} onRetry={onRetry} />
    </div>
  );
};

export default ErrorMessage;