import { Card, CardContent } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';
import { Check, Circle, Spinner } from '@phosphor-icons/react';

interface Step {
  id: string;
  title: string;
  subtitle?: string;
  status: 'pending' | 'active' | 'completed' | 'error';
}

interface CheckoutStepperProps {
  data: {
    current_step: number;
    steps: Step[];
  };
  emphasis?: 'low' | 'medium' | 'high';
}

export function CheckoutStepper({ data, emphasis = 'medium' }: CheckoutStepperProps) {
  const getStepIcon = (step: Step, index: number) => {
    if (step.status === 'completed') {
      return <Check size={20} weight="bold" className="text-primary-foreground" />;
    }
    if (step.status === 'active') {
      return <Spinner size={20} className="text-primary-foreground animate-spin" />;
    }
    if (step.status === 'error') {
      return <span className="text-primary-foreground font-bold text-sm">!</span>;
    }
    return <span className="text-muted-foreground text-sm font-semibold">{index + 1}</span>;
  };

  const getStepColor = (step: Step) => {
    if (step.status === 'completed') return 'bg-primary';
    if (step.status === 'active') return 'bg-primary';
    if (step.status === 'error') return 'bg-destructive';
    return 'bg-muted';
  };

  const getConnectorColor = (currentStep: Step, nextStep: Step) => {
    if (currentStep.status === 'completed') return 'bg-primary';
    return 'bg-muted';
  };

  return (
    <Card className={emphasis === 'high' ? 'border-2 shadow-lg' : ''}>
      <CardContent className="p-6">
        <div className="mb-4">
          <h3 className="text-lg font-bold">Checkout Progress</h3>
          <p className="text-sm text-muted-foreground">
            Step {data.current_step + 1} of {data.steps.length}
          </p>
        </div>

        <div className="space-y-4">
          {data.steps.map((step, index) => (
            <div key={step.id}>
              <div className="flex items-start gap-4">
                {/* Step Icon */}
                <div className={`
                  flex-shrink-0 w-10 h-10 rounded-full flex items-center justify-center
                  ${getStepColor(step)} transition-colors
                `}>
                  {getStepIcon(step, index)}
                </div>

                {/* Step Content */}
                <div className="flex-1 min-w-0">
                  <div className="flex items-center gap-2">
                    <h4 className={`font-semibold ${
                      step.status === 'active' ? 'text-foreground' : 'text-muted-foreground'
                    }`}>
                      {step.title}
                    </h4>
                    {step.status === 'active' && (
                      <Badge variant="default" className="text-xs">In progress</Badge>
                    )}
                    {step.status === 'error' && (
                      <Badge variant="destructive" className="text-xs">Error</Badge>
                    )}
                  </div>
                  {step.subtitle && (
                    <p className="text-sm text-muted-foreground mt-1">{step.subtitle}</p>
                  )}
                </div>
              </div>

              {/* Connector Line */}
              {index < data.steps.length - 1 && (
                <div className="ml-5 h-6 w-0.5 bg-muted my-1 transition-colors"
                  style={{
                    backgroundColor: getConnectorColor(step, data.steps[index + 1]) === 'bg-primary'
                      ? 'hsl(var(--primary))'
                      : 'hsl(var(--muted))'
                  }}
                />
              )}
            </div>
          ))}
        </div>
      </CardContent>
    </Card>
  );
}
