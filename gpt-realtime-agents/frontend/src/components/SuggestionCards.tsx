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
      className={`cursor-pointer transition-all hover:shadow-xl border-2 h-full flex flex-col overflow-hidden group ${
        disabled ? 'opacity-50 cursor-not-allowed' : 'hover:border-teal-500 hover:scale-105'
      }`}
      onClick={() => handleCardClick(card)}
    >
      <div className="relative h-full">
        {/* Background Image */}
        {card.image && (
          <div
            className="absolute inset-0 bg-cover bg-center transition-transform group-hover:scale-110"
            style={{ backgroundImage: `url(${card.image})` }}
          />
        )}

        {/* Gradient Overlay */}
        <div className="absolute inset-0 bg-gradient-to-t from-black/80 via-black/40 to-black/20" />

        {/* Content */}
        <CardContent className="relative p-4 flex flex-col justify-end h-full text-left z-10">
          <div className="text-white/90 mb-2">
            {renderIcon(card.icon)}
          </div>
          <h3 className="font-bold text-base mb-1 leading-tight text-white drop-shadow-lg">{card.title}</h3>
          <p className="text-sm text-white/90 leading-tight">{card.subtitle}</p>
        </CardContent>
      </div>
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
