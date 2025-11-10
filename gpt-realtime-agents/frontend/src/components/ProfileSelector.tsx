import { useState, useEffect } from 'react';
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from '@/components/ui/select';
import { Label } from '@/components/ui/label';
import { User } from '@phosphor-icons/react';

interface CustomerProfile {
  account_number: string;
  name: string;
  scenario: string;
}

interface ProfileSelectorProps {
  selectedProfile: string | null;
  onProfileChange: (accountNumber: string | null) => void;
  disabled?: boolean;
}

export function ProfileSelector({ selectedProfile, onProfileChange, disabled }: ProfileSelectorProps) {
  const [profiles, setProfiles] = useState<CustomerProfile[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Fetch customer profiles from backend
    fetch('/api/customer-profiles')
      .then(res => res.json())
      .then(data => {
        setProfiles(data.profiles || []);
        setLoading(false);
      })
      .catch(err => {
        console.error('Failed to load customer profiles:', err);
        setLoading(false);
      });
  }, []);

  return (
    <div className="flex items-center gap-3 px-4 py-2 bg-muted/50 border-b">
      <User size={20} className="text-muted-foreground" />
      <Label htmlFor="profile-select" className="text-sm font-medium whitespace-nowrap">
        Test Profile:
      </Label>
      <Select
        value={selectedProfile || 'none'}
        onValueChange={(value) => onProfileChange(value === 'none' ? null : value)}
        disabled={disabled || loading}
      >
        <SelectTrigger id="profile-select" className="w-[400px]">
          <SelectValue placeholder={loading ? "Loading profiles..." : "Select customer profile..."} />
        </SelectTrigger>
        <SelectContent>
          <SelectItem value="none">
            <span className="text-muted-foreground">No Profile (Anonymous)</span>
          </SelectItem>
          {profiles.map((profile) => (
            <SelectItem key={profile.account_number} value={profile.account_number}>
              <div className="flex flex-col">
                <span className="font-medium">{profile.name}</span>
                <span className="text-xs text-muted-foreground">{profile.scenario}</span>
              </div>
            </SelectItem>
          ))}
        </SelectContent>
      </Select>
    </div>
  );
}
