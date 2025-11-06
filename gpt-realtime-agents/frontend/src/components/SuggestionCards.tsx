import { Card, CardContent } from '@/components/ui/card';
import { SuggestionCard } from '@/lib/types';
import { DEFAULT_SUGGESTION_CARDS } from '@/lib/constants';
import * as PhosphorIcons from '@phosphor-icons/react';

interface SuggestionCardsProps {
  onSuggestionClick: (prompt: string) => void;
  disabled?: boolean;
}

export function SuggestionCards({
  onSuggestionClick,
  disabled = false
}: SuggestionCardsProps) {
  const handleCardClick = (card: SuggestionCard) => {
    if (disabled) return;
    onSuggestionClick(card.prompt);
  };

  const renderIcon = (iconName: string) => {
    const IconComponent = (PhosphorIcons as any)[iconName];
    return IconComponent ? <IconComponent size={20} weight="regular" /> : null;
  };

  const renderCard = (card: SuggestionCard) => (
    <Card
      key={card.id}
      className={`cursor-pointer transition-all hover:shadow-md border h-full flex flex-col @container ${
        disabled ? 'opacity-50 cursor-not-allowed' : 'hover:border-primary/50 hover:bg-accent/10'
      }`}
      onClick={() => handleCardClick(card)}
    >
      <CardContent className="p-3 flex flex-col items-center justify-center h-full text-center">
        <div className="text-primary mb-2">
          {renderIcon(card.icon)}
        </div>
        <h3 className="font-semibold text-sm mb-1 leading-tight">{card.title}</h3>
        <p className="text-xs text-muted-foreground leading-tight">{card.subtitle}</p>
      </CardContent>
    </Card>
  );

  return (
    <div className="h-full flex flex-col">
      <div className="flex items-center justify-between mb-3 flex-shrink-0">
        <h2 className="text-base font-semibold">How can I help you today?</h2>
      </div>

      <div className="grid grid-cols-2 gap-3 flex-1 min-h-0 overflow-y-auto">
        {DEFAULT_SUGGESTION_CARDS.map(renderCard)}
      </div>
    </div>
  );
}
