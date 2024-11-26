export interface Task {
    id: number | null;
    user_id: string;
    name: string;
    tags: Set<string> | null;
    comments: string | null;
    created_at: string | null;
    state: string;
    deadline: string | null;

}