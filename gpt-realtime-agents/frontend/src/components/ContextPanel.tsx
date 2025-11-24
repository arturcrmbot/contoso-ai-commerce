import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Button } from '@/components/ui/button';
import { Badge } from '@/components/ui/badge';
import { Separator } from '@/components/ui/separator';
import { CustomerProfile, RecentAction } from '@/lib/types';
import { Copy, ArrowCounterClockwise, User, CreditCard, Package } from '@phosphor-icons/react';

interface ContextPanelProps {
  customerProfile?: CustomerProfile;
  recentActions: RecentAction[];
  caseNotes: string[];
  onCopyNotes: () => void;
  onUndoAction: (actionId: string) => void;
}

export function ContextPanel({ 
  customerProfile, 
  recentActions, 
  caseNotes, 
  onCopyNotes, 
  onUndoAction 
}: ContextPanelProps) {
  const formatTime = (timestamp: number) => {
    return new Date(timestamp).toLocaleTimeString([], { 
      hour: '2-digit', 
      minute: '2-digit' 
    });
  };

  return (
    <div className="space-y-6 p-1">
      {/* Customer Profile */}
      {customerProfile && (
        <Card className="border-0 shadow-md rounded-2xl overflow-hidden bg-white/80 backdrop-blur-sm">
          <div className="h-2 bg-gradient-to-r from-teal-500 to-cyan-500" />
          <CardHeader className="pb-3 pt-4">
            <CardTitle className="text-sm font-bold flex items-center gap-2 text-gray-800 uppercase tracking-wider">
              <User size={16} weight="bold" className="text-teal-600" />
              Traveler Profile
            </CardTitle>
          </CardHeader>
          <CardContent className="space-y-4">
            <div>
              <div className="font-bold text-lg text-gray-900">{customerProfile.name}</div>
              <div className="text-xs font-medium text-gray-500 flex items-center gap-1">
                Account <span className="font-mono bg-gray-100 px-1 rounded">••••{customerProfile.accountId.slice(-4)}</span>
              </div>
            </div>
            
            <div className="flex items-center gap-2 p-2 bg-teal-50 rounded-lg border border-teal-100">
              <Package size={16} weight="fill" className="text-teal-600" />
              <span className="text-sm font-medium text-teal-900">{customerProfile.plan} Member</span>
            </div>
            
            <div className="flex items-center justify-between pt-2 border-t border-gray-100">
              <div className="flex items-center gap-2">
                <CreditCard size={16} className="text-gray-400" />
                <span className="text-sm font-semibold text-gray-700">${customerProfile.balance}</span>
              </div>
              {customerProfile.isVerified && (
                <Badge variant="secondary" className="bg-green-100 text-green-700 hover:bg-green-200 border-0 text-[10px] font-bold px-2 py-0.5">
                  VERIFIED
                </Badge>
              )}
            </div>
          </CardContent>
        </Card>
      )}

      {/* Recent Actions */}
      <Card className="border-0 shadow-md rounded-2xl overflow-hidden bg-white/80 backdrop-blur-sm">
        <CardHeader className="pb-3 pt-4 border-b border-gray-50">
          <CardTitle className="text-sm font-bold text-gray-800 uppercase tracking-wider">Recent Activity</CardTitle>
        </CardHeader>
        <CardContent className="pt-0">
          {recentActions.length === 0 ? (
            <div className="text-xs text-gray-400 text-center py-8 italic">
              No recent actions recorded
            </div>
          ) : (
            <div className="divide-y divide-gray-50">
              {recentActions.map((action) => (
                <div key={action.id} className="py-3 first:pt-4 last:pb-2">
                  <div className="flex items-start justify-between gap-3">
                    <div className="flex-1 min-w-0">
                      <div className="text-sm font-semibold text-gray-800 truncate">{action.action}</div>
                      <div className="text-xs text-gray-500 mt-0.5 line-clamp-2">
                        {action.details}
                      </div>
                      <div className="text-[10px] font-medium text-gray-400 mt-1.5 flex items-center gap-1">
                        <div className="w-1 h-1 rounded-full bg-gray-300" />
                        {formatTime(action.timestamp)}
                      </div>
                    </div>
                    
                    {action.canUndo && (
                      <Button
                        variant="ghost"
                        size="sm"
                        className="h-7 w-7 p-0 flex-shrink-0 text-gray-400 hover:text-red-600 hover:bg-red-50 rounded-full transition-colors"
                        onClick={() => onUndoAction(action.id)}
                        title="Undo action"
                      >
                        <ArrowCounterClockwise size={14} weight="bold" />
                      </Button>
                    )}
                  </div>
                </div>
              ))}
            </div>
          )}
        </CardContent>
      </Card>

      {/* Case Notes */}
      <Card className="border-0 shadow-md rounded-2xl overflow-hidden bg-white/80 backdrop-blur-sm">
        <CardHeader className="pb-3 pt-4 border-b border-gray-50 bg-gray-50/50">
          <CardTitle className="text-sm font-bold flex items-center justify-between text-gray-800 uppercase tracking-wider">
            Session Notes
            <Button
              variant="ghost"
              size="sm"
              onClick={onCopyNotes}
              className="h-6 px-2 text-[10px] font-semibold text-teal-600 hover:text-teal-700 hover:bg-teal-50 rounded-full"
            >
              <Copy size={12} className="mr-1" weight="bold" />
              COPY
            </Button>
          </CardTitle>
        </CardHeader>
        <CardContent className="pt-4 bg-yellow-50/30 min-h-[100px]">
          {caseNotes.length === 0 ? (
            <div className="text-xs text-gray-400 text-center py-4 italic">
              No notes taken yet...
            </div>
          ) : (
            <div className="space-y-2">
              {caseNotes.map((note, index) => (
                <div key={index} className="text-xs p-2.5 bg-white border border-yellow-100 rounded-lg text-gray-600 shadow-sm">
                  <span className="text-yellow-500 mr-1.5">•</span> {note}
                </div>
              ))}
            </div>
          )}
        </CardContent>
      </Card>
    </div>
  );
}