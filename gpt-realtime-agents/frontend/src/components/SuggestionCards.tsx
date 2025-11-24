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
      className={`relative h-64 cursor-pointer overflow-hidden group border-0 rounded-xl shadow-md hover:shadow-xl transition-all duration-300 ${
        disabled ? 'opacity-50 cursor-not-allowed' : 'hover:-translate-y-1'
      }`}
      onClick={() => handleCardClick(card)}
    >
      {/* Background Image */}
      {card.image && (
        <div
          className="absolute inset-0 bg-cover bg-center transition-transform duration-700 group-hover:scale-110"
          style={{ backgroundImage: `url(${card.image})` }}
        />
      )}

      {/* Gradient Overlay */}
      <div className="absolute inset-0 bg-gradient-to-t from-black/90 via-black/40 to-transparent opacity-80 group-hover:opacity-90 transition-opacity" />

      {/* Content */}
      <CardContent className="relative h-full flex flex-col justify-end p-6 text-white z-10">
        <div className="mb-3 transform translate-y-2 group-hover:translate-y-0 transition-transform duration-300">
          <div className="bg-white/20 w-10 h-10 rounded-full flex items-center justify-center backdrop-blur-sm mb-3">
            {renderIcon(card.icon)}
          </div>
          <h3 className="font-bold text-xl mb-1 leading-tight">{card.title}</h3>
          <p className="text-sm text-white/80 font-medium">{card.subtitle}</p>
        </div>
      </CardContent>
    </Card>
  );

  return (
    <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6 pb-8">
      {DEFAULT_SUGGESTION_CARDS.map(renderCard)}
    </div>
  );
}
