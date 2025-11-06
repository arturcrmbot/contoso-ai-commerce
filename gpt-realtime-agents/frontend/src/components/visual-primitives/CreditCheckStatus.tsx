import { Card, CardContent } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';
import { CheckCircle, XCircle, Spinner, Info } from '@phosphor-icons/react';

interface CreditCheckStatusProps {
  data: {
    status: 'checking' | 'approved' | 'declined' | 'review_required';
    message?: string;
    credit_limit?: number;
    reasons?: string[];
    next_steps?: string[];
  };
  emphasis?: 'low' | 'medium' | 'high' | 'critical';
}

export function CreditCheckStatus({ data, emphasis = 'high' }: CreditCheckStatusProps) {
  const getStatusConfig = () => {
    switch (data.status) {
      case 'checking':
        return {
          icon: <Spinner size={48} className="text-primary animate-spin" />,
          title: 'Checking Your Credit',
          color: 'text-primary',
          bgColor: 'bg-primary/10',
          badge: 'secondary'
        };
      case 'approved':
        return {
          icon: <CheckCircle size={48} weight="fill" className="text-green-600" />,
          title: 'Credit Approved!',
          color: 'text-green-600',
          bgColor: 'bg-green-100',
          badge: 'default'
        };
      case 'declined':
        return {
          icon: <XCircle size={48} weight="fill" className="text-destructive" />,
          title: 'Credit Check Declined',
          color: 'text-destructive',
          bgColor: 'bg-destructive/10',
          badge: 'destructive'
        };
      case 'review_required':
        return {
          icon: <Info size={48} weight="fill" className="text-yellow-600" />,
          title: 'Manual Review Required',
          color: 'text-yellow-600',
          bgColor: 'bg-yellow-100',
          badge: 'secondary'
        };
    }
  };

  const config = getStatusConfig();
  const emphasisClasses = {
    low: '',
    medium: 'border-2',
    high: 'border-2 shadow-lg',
    critical: 'border-4 shadow-2xl'
  };

  return (
    <Card className={`${emphasisClasses[emphasis]} transition-all`}>
      <CardContent className="p-6">
        {/* Status Icon & Title */}
        <div className="text-center mb-6">
          <div className={`inline-flex items-center justify-center w-20 h-20 rounded-full ${config.bgColor} mb-4`}>
            {config.icon}
          </div>
          <h3 className={`text-2xl font-bold mb-2 ${config.color}`}>
            {config.title}
          </h3>
          {data.message && (
            <p className="text-sm text-muted-foreground">{data.message}</p>
          )}
        </div>

        {/* Credit Limit (if approved) */}
        {data.status === 'approved' && data.credit_limit && (
          <div className="bg-muted rounded-lg p-4 mb-4">
            <p className="text-sm text-muted-foreground mb-1">Approved Credit Limit</p>
            <p className="text-3xl font-bold">£{data.credit_limit.toLocaleString()}</p>
          </div>
        )}

        {/* Reasons (if declined) */}
        {data.reasons && data.reasons.length > 0 && (
          <div className="mb-4">
            <h4 className="text-sm font-semibold mb-2">Reasons:</h4>
            <ul className="space-y-1">
              {data.reasons.map((reason, idx) => (
                <li key={idx} className="text-sm text-muted-foreground flex items-start gap-2">
                  <span className="text-destructive">•</span>
                  {reason}
                </li>
              ))}
            </ul>
          </div>
        )}

        {/* Next Steps */}
        {data.next_steps && data.next_steps.length > 0 && (
          <div className="border-t pt-4">
            <h4 className="text-sm font-semibold mb-2">Next Steps:</h4>
            <ul className="space-y-1">
              {data.next_steps.map((step, idx) => (
                <li key={idx} className="text-sm text-muted-foreground flex items-start gap-2">
                  <span className={config.color}>✓</span>
                  {step}
                </li>
              ))}
            </ul>
          </div>
        )}
      </CardContent>
    </Card>
  );
}
